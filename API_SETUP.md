# Flask API Setup Guide

This guide will help you set up and use the Flask REST API for the NSE/BSE Data Downloader.

## 📋 Quick Setup

### 1. Install Dependencies

Make sure you have all required packages installed:

```bash
pip install -r requirements.txt
```

This will install:
- Flask >= 2.3.0
- Flask-CORS >= 4.0.0
- All other project dependencies

### 2. Verify Configuration

Ensure `config.yaml` exists in the project root with proper settings. The API uses the same configuration as the GUI application.

### 3. Start the API Server

**Windows:**
```bash
start_api.bat
```

**Linux/Mac:**
```bash
./start_api.sh
```

**Or directly with Python:**
```bash
python api.py

# With custom host/port
python api.py --host 0.0.0.0 --port 8080

# With debug mode
python api.py --debug
```

## 🧪 Testing the API

### Option 1: Interactive Web Interface

1. Start the API server
2. Open `api_test.html` in your web browser
3. Use the interactive interface to test endpoints

### Option 2: Python Test Script

```bash
# Run all tests
python test_api.py

# Run specific test
python test_api.py --test health

# Test with data refresh (downloads data)
python test_api.py --refresh
```

### Option 3: cURL Commands

```bash
# Health check
curl http://localhost:5000/health

# Get status
curl http://localhost:5000/status/NSE_EQ

# Refresh data
curl -X POST http://localhost:5000/refresh/NSE_EQ \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2025-10-01", "end_date": "2025-11-02"}'
```

### Option 4: Postman Collection

Import `NSE_BSE_API.postman_collection.json` into Postman for a complete set of pre-configured API requests.

## 📁 New Files Created

### Core API Files
- **`api.py`** - Main Flask application with all API endpoints
- **`API_README.md`** - Comprehensive API documentation
- **`API_SETUP.md`** - This setup guide

### Testing & Utilities
- **`test_api.py`** - Python script for automated API testing
- **`api_test.html`** - Interactive web interface for API testing
- **`NSE_BSE_API.postman_collection.json`** - Postman collection for API testing

### Startup Scripts
- **`start_api.bat`** - Windows startup script
- **`start_api.sh`** - Linux/Mac startup script (executable)

## 🔧 Configuration Options

The API can be configured via command-line arguments:

```bash
python api.py --help
```

**Available options:**
- `--host`: Host to bind to (default: 0.0.0.0)
- `--port`: Port to bind to (default: 5000)
- `--debug`: Enable debug mode

## 🌐 API Endpoints Overview

### Information Endpoints
- `GET /` - API information
- `GET /health` - Health check
- `GET /config` - Get configuration

### Status Endpoints
- `GET /status` - All exchange status
- `GET /status/<exchange>` - Specific exchange status
- `GET /summary` - Data summary

### Refresh Endpoints
- `POST /refresh` - Refresh multiple exchanges
- `POST /refresh/<exchange>` - Refresh specific exchange

## 🔐 Production Deployment

For production use, consider:

1. **Use a production WSGI server:**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 api:app
   ```

2. **Add authentication** for secure access

3. **Enable HTTPS** using a reverse proxy (nginx, Apache)

4. **Configure firewall** to restrict access

5. **Set up logging** for production monitoring

## 📖 Documentation

- **API Reference**: See `API_README.md` for detailed endpoint documentation
- **Examples**: Check `API_README.md` for usage examples in various languages

## 🆘 Troubleshooting

### Port Already in Use
If port 5000 is already in use:
```bash
python api.py --port 8080
```

### Import Errors
Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Configuration Not Found
Ensure `config.yaml` exists in the project root directory.

### Connection Refused
- Check if the API server is running
- Verify the correct host and port
- Check firewall settings

## 💡 Usage Tips

1. **Auto-refresh on schedule**: Use cron (Linux) or Task Scheduler (Windows) to schedule data refreshes:
   ```bash
   # Example cron entry (run daily at 7 PM)
   0 19 * * * curl -X POST http://localhost:5000/refresh
   ```

2. **Monitor data status**: Set up monitoring to check database status:
   ```bash
   curl http://localhost:5000/status | jq
   ```

3. **Selective refresh**: Refresh only specific exchanges to save time:
   ```bash
   curl -X POST http://localhost:5000/refresh \
     -H "Content-Type: application/json" \
     -d '{"exchanges": ["NSE_EQ"]}'
   ```

## 🎯 Next Steps

1. Start the API server
2. Test using the web interface or test script
3. Integrate with your applications
4. Set up automated data refresh
5. Monitor using status endpoints

For more details, see `API_README.md`!

