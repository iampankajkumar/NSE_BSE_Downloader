@echo off
REM Start the NSE/BSE Data Downloader API Server
REM This script is for Windows

echo Starting NSE/BSE Data Downloader API...
echo.
echo API will be available at: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

REM Activate virtual environment if it exists
if exist venv\Scripts\activate.bat (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

REM Start the Flask API
python api.py

pause

