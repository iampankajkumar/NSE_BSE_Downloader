# NSE/BSE Data Downloader - Flask API Documentation

A RESTful API to manage and refresh NSE/BSE market data programmatically.

## Quick Start

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the API Server

#### Basic Usage
```bash
python api.py
```
The API will start on `http://localhost:5000`

#### Custom Host/Port
```bash
python api.py --host 0.0.0.0 --port 8080
```

#### Debug Mode
```bash
python api.py --debug
```

## API Endpoints

### 1. Root Endpoint
**GET /** - API information and available endpoints

**Response:**
```json
{
  "message": "NSE/BSE Data Downloader API",
  "version": "1.0.0",
  "endpoints": { ... }
}
```

### 2. Health Check
**GET /health** - Check API health status

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-11-03T10:30:00",
  "config_loaded": true,
  "data_manager_ready": true
}
```

### 3. Data Status

#### Get All Exchange Status
**GET /status** - Get data status for all exchanges

**Response:**
```json
{
  "status": "success",
  "timestamp": "2025-11-03T10:30:00",
  "exchanges": {
    "NSE_EQ": {
      "last_date": "2025-11-02",
      "file_count": 120,
      "is_first_run": false,
      "data_path": "/path/to/NSE/EQ"
    },
    ...
  }
}
```

#### Get Specific Exchange Status
**GET /status/NSE_EQ** - Get data status for specific exchange

**Path Parameters:**
- `exchange`: Exchange name (NSE_EQ, NSE_FO, NSE_SME, NSE_INDEX, BSE_EQ, BSE_INDEX)

**Response:**
```json
{
  "status": "success",
  "exchange": "NSE_EQ",
  "data": {
    "last_date": "2025-11-02",
    "file_count": 120,
    "is_first_run": false,
    "is_up_to_date": true,
    "status_message": "Database is up-to-date. Last file date: 2025-11-02",
    "data_path": "/path/to/NSE/EQ"
  }
}
```

### 4. Data Refresh

#### Refresh All Exchanges
**POST /refresh** - Refresh data for multiple exchanges

**Request Body (all optional):**
```json
{
  "exchanges": ["NSE_EQ", "NSE_FO"],
  "start_date": "2025-10-01",
  "end_date": "2025-11-02"
}
```

**Parameters:**
- `exchanges` (optional): Array of exchange names. Default: all exchanges
- `start_date` (optional): Start date in YYYY-MM-DD format
- `end_date` (optional): End date in YYYY-MM-DD format

**Response:**
```json
{
  "status": "success",
  "timestamp": "2025-11-03T10:30:00",
  "summary": "2/2 exchanges refreshed successfully",
  "results": {
    "NSE_EQ": {
      "success": true,
      "message": "Data refreshed successfully",
      "dates_processed": 15,
      "start_date": "2025-10-01",
      "end_date": "2025-11-02",
      "last_file_date": "2025-11-02",
      "total_files": 135
    },
    ...
  }
}
```

#### Refresh Specific Exchange
**POST /refresh/NSE_EQ** - Refresh data for specific exchange

**Path Parameters:**
- `exchange`: Exchange name

**Request Body (all optional):**
```json
{
  "start_date": "2025-10-01",
  "end_date": "2025-11-02"
}
```

**Response:**
```json
{
  "status": "success",
  "timestamp": "2025-11-03T10:30:00",
  "exchange": "NSE_EQ",
  "data": {
    "success": true,
    "message": "Data refreshed successfully",
    "dates_processed": 15,
    "start_date": "2025-10-01",
    "end_date": "2025-11-02",
    "last_file_date": "2025-11-02",
    "total_files": 135
  }
}
```

### 5. Data Summary
**GET /summary** - Get comprehensive data summary

**Response:**
```json
{
  "status": "success",
  "timestamp": "2025-11-03T10:30:00",
  "statistics": {
    "total_exchanges": 6,
    "exchanges_with_data": 4,
    "total_files": 480
  },
  "exchanges": { ... }
}
```

### 6. Configuration
**GET /config** - Get current configuration

**Response:**
```json
{
  "status": "success",
  "config": {
    "base_data_path": "/path/to/NSE_BSE_Data",
    "available_exchanges": ["NSE_EQ", "NSE_FO", ...],
    "download_settings": {
      "max_concurrent_downloads": 1,
      "retry_attempts": 3,
      "timeout_seconds": 5
    },
    "date_settings": {
      "base_start_date": "2025-07-15",
      "weekend_skip": true,
      "holiday_skip": true
    }
  }
}
```

## Usage Examples

### Using cURL

#### Check API Health
```bash
curl http://localhost:5000/health
```

#### Get Status for NSE_EQ
```bash
curl http://localhost:5000/status/NSE_EQ
```

#### Refresh All Exchanges
```bash
curl -X POST http://localhost:5000/refresh \
  -H "Content-Type: application/json"
```

#### Refresh Specific Exchange with Date Range
```bash
curl -X POST http://localhost:5000/refresh/NSE_EQ \
  -H "Content-Type: application/json" \
  -d '{
    "start_date": "2025-10-01",
    "end_date": "2025-11-02"
  }'
```

#### Refresh Multiple Exchanges
```bash
curl -X POST http://localhost:5000/refresh \
  -H "Content-Type: application/json" \
  -d '{
    "exchanges": ["NSE_EQ", "NSE_FO", "BSE_EQ"]
  }'
```

### Using Python Requests

```python
import requests

BASE_URL = "http://localhost:5000"

# Check health
response = requests.get(f"{BASE_URL}/health")
print(response.json())

# Get status
response = requests.get(f"{BASE_URL}/status/NSE_EQ")
print(response.json())

# Refresh data
response = requests.post(
    f"{BASE_URL}/refresh/NSE_EQ",
    json={
        "start_date": "2025-10-01",
        "end_date": "2025-11-02"
    }
)
print(response.json())

# Refresh all exchanges
response = requests.post(
    f"{BASE_URL}/refresh",
    json={
        "exchanges": ["NSE_EQ", "BSE_EQ"]
    }
)
print(response.json())
```

### Using JavaScript/Fetch

```javascript
const BASE_URL = 'http://localhost:5000';

// Check health
fetch(`${BASE_URL}/health`)
  .then(response => response.json())
  .then(data => console.log(data));

// Refresh data
fetch(`${BASE_URL}/refresh/NSE_EQ`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    start_date: '2025-10-01',
    end_date: '2025-11-02'
  })
})
  .then(response => response.json())
  .then(data => console.log(data));
```

## Available Exchanges

- `NSE_EQ` - NSE Equity
- `NSE_FO` - NSE Futures & Options
- `NSE_SME` - NSE SME
- `NSE_INDEX` - NSE Indices
- `BSE_EQ` - BSE Equity
- `BSE_INDEX` - BSE Indices

## Error Handling

All endpoints return appropriate HTTP status codes:

- `200` - Success
- `400` - Bad Request (invalid parameters)
- `404` - Not Found (invalid endpoint)
- `500` - Internal Server Error

Error responses follow this format:
```json
{
  "status": "error",
  "message": "Error description"
}
```

## Configuration

The API uses the same `config.yaml` file as the GUI application. Ensure the configuration file exists in the project root.

## Logging

The API logs all operations to both console and the log file specified in `config.yaml`. Use `--debug` flag for verbose logging during development.

## Production Deployment

For production deployment, use a production-grade WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 api:app
```

Or use uWSGI:
```bash
pip install uwsgi
uwsgi --http 0.0.0.0:5000 --wsgi-file api.py --callable app --processes 4
```

## Security Considerations

1. **Authentication**: Consider adding authentication for production use
2. **Rate Limiting**: Implement rate limiting to prevent abuse
3. **CORS**: Configure CORS appropriately for your use case
4. **HTTPS**: Use HTTPS in production
5. **Firewall**: Restrict access to trusted IPs if needed

## Notes

- The API automatically respects weekend and holiday settings from `config.yaml`
- Data refresh operations may take time depending on the date range
- All dates must be in `YYYY-MM-DD` format
- The API uses async operations internally for efficient downloads

