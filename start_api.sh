#!/bin/bash
# Start the NSE/BSE Data Downloader API Server
# This script is for Linux/Mac

echo "Starting NSE/BSE Data Downloader API..."
echo ""
echo "API will be available at: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Start the Flask API
python api.py

