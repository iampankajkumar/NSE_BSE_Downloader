#!/usr/bin/env python3
"""
NSE/BSE Data Downloader - Flask API
Exposes REST endpoints for data refresh and management
"""

import sys
import asyncio
from pathlib import Path
from datetime import datetime, date
from typing import Optional, Dict, Any
import logging

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from src.core.config import Config
from src.core.data_manager import DataManager
from src.downloaders.nse_eq_downloader import NSEEQDownloader
from src.downloaders.nse_fo_downloader import NSEFODownloader
from src.downloaders.nse_sme_downloader import NSESMEDownloader
from src.downloaders.nse_index_downloader import NSEIndexDownloader
from src.downloaders.bse_eq_downloader import BSEEQDownloader
from src.downloaders.bse_index_downloader import BSEIndexDownloader

# Initialize Flask app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Enable CORS for all routes
CORS(app)

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize configuration
config_path = Path(__file__).parent / "config.yaml"
config = Config(str(config_path))
data_manager = DataManager(config)

# Downloader mapping
DOWNLOADER_MAP = {
    'NSE_EQ': NSEEQDownloader,
    'NSE_FO': NSEFODownloader,
    'NSE_SME': NSESMEDownloader,
    'NSE_INDEX': NSEIndexDownloader,
    'BSE_EQ': BSEEQDownloader,
    'BSE_INDEX': BSEIndexDownloader
}


def parse_date(date_str: Optional[str]) -> Optional[date]:
    """Parse date string in YYYY-MM-DD format"""
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}. Use YYYY-MM-DD format")


@app.route('/', methods=['GET'])
def index():
    """Serve the launcher page or API information"""
    # If browser request, serve HTML
    if 'text/html' in request.headers.get('Accept', ''):
        return send_from_directory('.', 'launch_ui.html')
    
    # Otherwise return JSON API info
    return jsonify({
        'message': 'NSE/BSE Data Downloader API',
        'version': '1.0.0',
        'web_ui': {
            'launcher': 'http://localhost:5000/',
            'dashboard': 'http://localhost:5000/dashboard',
            'api_test': 'http://localhost:5000/api-test'
        },
        'endpoints': {
            'GET /': 'API information or launcher page',
            'GET /dashboard': 'Main web dashboard',
            'GET /api-test': 'API testing interface',
            'GET /health': 'Health check',
            'GET /status': 'Get data status for all exchanges',
            'GET /status/<exchange>': 'Get data status for specific exchange',
            'POST /refresh': 'Refresh data for selected exchanges',
            'POST /refresh/<exchange>': 'Refresh data for specific exchange',
            'GET /summary': 'Get data summary',
            'GET /config': 'Get current configuration'
        }
    })


@app.route('/dashboard')
def dashboard():
    """Serve the main dashboard"""
    return send_from_directory('.', 'web_ui.html')


@app.route('/api-test')
def api_test():
    """Serve the API test interface"""
    return send_from_directory('.', 'api_test.html')


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'config_loaded': config is not None,
        'data_manager_ready': data_manager is not None
    })


@app.route('/status', methods=['GET'])
def get_all_status():
    """Get data status for all exchanges"""
    try:
        summary = data_manager.get_data_summary()
        return jsonify({
            'status': 'success',
            'timestamp': datetime.now().isoformat(),
            'exchanges': summary
        })
    except Exception as e:
        logger.error(f"Error getting status: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/status/<exchange>', methods=['GET'])
def get_exchange_status(exchange):
    """Get data status for specific exchange"""
    try:
        exchange = exchange.upper()
        
        if exchange not in DOWNLOADER_MAP:
            return jsonify({
                'status': 'error',
                'message': f'Invalid exchange: {exchange}. Valid exchanges: {", ".join(DOWNLOADER_MAP.keys())}'
            }), 400
        
        exchange_name, segment = exchange.split('_', 1)
        
        # Get status information
        last_date = data_manager.get_last_file_date(exchange_name, segment)
        file_count = data_manager.get_file_count(exchange_name, segment)
        is_first = data_manager.is_first_run(exchange_name, segment)
        is_up_to_date, status_message = data_manager.is_database_up_to_date(exchange_name, segment)
        
        return jsonify({
            'status': 'success',
            'exchange': exchange,
            'data': {
                'last_date': last_date.strftime('%Y-%m-%d') if last_date else None,
                'file_count': file_count,
                'is_first_run': is_first,
                'is_up_to_date': is_up_to_date,
                'status_message': status_message,
                'data_path': str(config.get_data_path(exchange_name, segment))
            }
        })
    except Exception as e:
        logger.error(f"Error getting status for {exchange}: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/refresh', methods=['POST'])
def refresh_all():
    """Refresh data for multiple exchanges"""
    try:
        # Get request parameters
        data = request.get_json() or {}
        exchanges = data.get('exchanges', list(DOWNLOADER_MAP.keys()))
        start_date = parse_date(data.get('start_date'))
        end_date = parse_date(data.get('end_date'))
        
        # Validate exchanges
        invalid_exchanges = [ex for ex in exchanges if ex.upper() not in DOWNLOADER_MAP]
        if invalid_exchanges:
            return jsonify({
                'status': 'error',
                'message': f'Invalid exchanges: {", ".join(invalid_exchanges)}. Valid exchanges: {", ".join(DOWNLOADER_MAP.keys())}'
            }), 400
        
        # Process each exchange
        results = {}
        for exchange in exchanges:
            exchange = exchange.upper()
            try:
                result = _refresh_exchange(exchange, start_date, end_date)
                results[exchange] = result
            except Exception as e:
                logger.error(f"Error refreshing {exchange}: {e}")
                results[exchange] = {
                    'success': False,
                    'error': str(e)
                }
        
        # Determine overall success
        success_count = sum(1 for r in results.values() if r.get('success', False))
        total_count = len(exchanges)
        
        return jsonify({
            'status': 'success' if success_count == total_count else 'partial',
            'timestamp': datetime.now().isoformat(),
            'summary': f'{success_count}/{total_count} exchanges refreshed successfully',
            'results': results
        })
        
    except ValueError as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400
    except Exception as e:
        logger.error(f"Error in refresh_all: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/refresh/<exchange>', methods=['POST'])
def refresh_exchange(exchange):
    """Refresh data for specific exchange"""
    try:
        exchange = exchange.upper()
        
        if exchange not in DOWNLOADER_MAP:
            return jsonify({
                'status': 'error',
                'message': f'Invalid exchange: {exchange}. Valid exchanges: {", ".join(DOWNLOADER_MAP.keys())}'
            }), 400
        
        # Get request parameters
        data = request.get_json() or {}
        start_date = parse_date(data.get('start_date'))
        end_date = parse_date(data.get('end_date'))
        
        # Refresh exchange
        result = _refresh_exchange(exchange, start_date, end_date)
        
        if result['success']:
            return jsonify({
                'status': 'success',
                'timestamp': datetime.now().isoformat(),
                'exchange': exchange,
                'data': result
            })
        else:
            return jsonify({
                'status': 'error',
                'exchange': exchange,
                'message': result.get('error', 'Unknown error')
            }), 500
            
    except ValueError as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400
    except Exception as e:
        logger.error(f"Error in refresh_exchange: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/summary', methods=['GET'])
def get_summary():
    """Get comprehensive data summary"""
    try:
        summary = data_manager.get_data_summary()
        
        # Calculate overall statistics
        total_files = sum(s.get('file_count', 0) for s in summary.values() if 'file_count' in s)
        exchanges_with_data = sum(1 for s in summary.values() if s.get('file_count', 0) > 0)
        
        return jsonify({
            'status': 'success',
            'timestamp': datetime.now().isoformat(),
            'statistics': {
                'total_exchanges': len(summary),
                'exchanges_with_data': exchanges_with_data,
                'total_files': total_files
            },
            'exchanges': summary
        })
    except Exception as e:
        logger.error(f"Error getting summary: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/config', methods=['GET'])
def get_config():
    """Get current configuration"""
    try:
        return jsonify({
            'status': 'success',
            'config': {
                'base_data_path': str(config.base_data_path),
                'available_exchanges': config.get_available_exchanges(),
                'download_settings': {
                    'max_concurrent_downloads': config.download_settings.max_concurrent_downloads,
                    'retry_attempts': config.download_settings.retry_attempts,
                    'timeout_seconds': config.download_settings.timeout_seconds
                },
                'date_settings': {
                    'base_start_date': config.date_settings.base_start_date,
                    'weekend_skip': config.date_settings.weekend_skip,
                    'holiday_skip': config.date_settings.holiday_skip
                }
            }
        })
    except Exception as e:
        logger.error(f"Error getting config: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


def _refresh_exchange(exchange: str, start_date: Optional[date] = None, 
                     end_date: Optional[date] = None) -> Dict[str, Any]:
    """
    Internal function to refresh data for a specific exchange
    
    Args:
        exchange: Exchange name (e.g., 'NSE_EQ')
        start_date: Optional start date
        end_date: Optional end date
        
    Returns:
        Dictionary with refresh results
    """
    try:
        exchange_name, segment = exchange.split('_', 1)
        
        # Calculate date range
        calc_start, calc_end = data_manager.calculate_date_range(
            exchange_name, segment, start_date, end_date
        )
        
        # Check if there's data to download
        if calc_start > calc_end:
            return {
                'success': True,
                'message': 'No new data to download',
                'dates_processed': 0,
                'start_date': calc_start.strftime('%Y-%m-%d'),
                'end_date': calc_end.strftime('%Y-%m-%d')
            }
        
        # Get working days
        working_days = data_manager.get_working_days(calc_start, calc_end)
        
        if not working_days:
            return {
                'success': True,
                'message': 'No trading days in date range',
                'dates_processed': 0,
                'start_date': calc_start.strftime('%Y-%m-%d'),
                'end_date': calc_end.strftime('%Y-%m-%d')
            }
        
        # Create downloader instance
        downloader_class = DOWNLOADER_MAP[exchange]
        downloader = downloader_class(config)
        
        # Run download
        logger.info(f"Starting download for {exchange}: {len(working_days)} working days")
        success = asyncio.run(downloader._download_implementation(working_days))
        
        # Get updated status
        last_date = data_manager.get_last_file_date(exchange_name, segment)
        file_count = data_manager.get_file_count(exchange_name, segment)
        
        return {
            'success': success,
            'message': 'Data refreshed successfully' if success else 'Some downloads failed',
            'dates_processed': len(working_days),
            'start_date': calc_start.strftime('%Y-%m-%d'),
            'end_date': calc_end.strftime('%Y-%m-%d'),
            'last_file_date': last_date.strftime('%Y-%m-%d') if last_date else None,
            'total_files': file_count
        }
        
    except Exception as e:
        logger.error(f"Error refreshing {exchange}: {e}")
        return {
            'success': False,
            'error': str(e)
        }


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Endpoint not found',
        'available_endpoints': [
            'GET /',
            'GET /health',
            'GET /status',
            'GET /status/<exchange>',
            'POST /refresh',
            'POST /refresh/<exchange>',
            'GET /summary',
            'GET /config'
        ]
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {error}")
    return jsonify({
        'status': 'error',
        'message': 'Internal server error'
    }), 500


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='NSE/BSE Data Downloader API')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to')
    parser.add_argument('--port', type=int, default=5000, help='Port to bind to')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    
    args = parser.parse_args()
    
    logger.info(f"Starting NSE/BSE Data Downloader API on {args.host}:{args.port}")
    app.run(host=args.host, port=args.port, debug=args.debug)

