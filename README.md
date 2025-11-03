# NSE/BSE Data Downloader v1.0.0

A professional application for downloading NSE and BSE market data with advanced processing capabilities.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![PyQt6](https://img.shields.io/badge/GUI-PyQt6-green.svg)
![License](https://img.shields.io/badge/license-GPL3.0-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)

## 🚀 Features

### **Multi-Exchange Support**
- **NSE**: Equity (EQ), Futures & Options (FO), SME, Index data
- **BSE**: Equity (EQ), Index data
- Parallel downloads for maximum efficiency

### **Advanced Data Processing**
- **Smart Append Operations**: Automatically combine related datasets
- **Memory Optimization**: Efficient handling of large datasets
- **Data Validation**: Ensures data integrity and consistency

### **User-Friendly Interface**
- **Modern GUI**: Built with PyQt6 for professional appearance
- **Web Dashboard**: Beautiful browser-based UI with real-time stats
- **REST API**: Flask-based API for programmatic access
- **Real-time Progress**: Live download progress and status updates
- **Customizable Settings**: User preferences saved automatically
- **Error Handling**: Comprehensive error reporting and recovery

### **Professional Features**
- **Automatic Updates**: Built-in update checking and notification
- **Concurrent Downloads**: Async processing for faster downloads
- **Weekend Support**: Optional weekend download attempts
- **Timeout Configuration**: Adjustable network timeout settings
- **RESTful API**: Expose data refresh functionality via HTTP endpoints

## 📦 Installation

### **Prerequisites**
- Python 3.8 or higher
- Internet connection for downloads

### **Quick Install**
```bash
# Clone the repository
git clone https://github.com/pparesh25/NSE_BSE_Downloader.git
cd NSE_BSE_Downloader

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### **Dependencies**
```
PyQt6>=6.4.0
aiohttp>=3.8.0
pandas>=1.5.0
numpy>=1.21.0
pyyaml>=6.0
Flask>=2.3.0
Flask-CORS>=4.0.0
```

## 🎯 Quick Start

### **Option 1: GUI Application**

#### **1. Launch Application**
```bash
python main.py
```

#### **2. Select Exchanges**
- ✅ Check desired exchanges (NSE EQ, NSE INDEX, BSE EQ, etc.)
- ⚙️ Configure append options if needed
- 📅 Set date range (optional)

#### **3. Download Data**
- 🚀 Click "Start Download"
- 📊 Monitor progress in real-time
- ✅ Data saved to `~/NSE_BSE_Data/`

### **Option 2: Web Dashboard (NEW!)**

#### **1. Start API Server**
```bash
python api.py
# Or use the convenience scripts:
# Windows: start_api.bat
# Linux/Mac: ./start_api.sh
```

#### **2. Launch Web UI**
- 🚀 Open `launch_ui.html` in your browser
- Or directly open `web_ui.html`
- 📊 Modern dashboard with real-time statistics
- 🎨 Beautiful, intuitive interface

#### **3. Features**
- ✅ Real-time exchange status monitoring
- 📈 Visual data statistics
- 🔄 Easy batch refresh operations
- 📋 Activity log with timestamps
- 📱 Fully responsive design

### **Option 3: REST API (Programmatic Access)**

#### **1. Access API**
- 🌐 API available at `http://localhost:5000`
- 📖 Full API documentation in [API_README.md](API_README.md)
- 🧪 Test interface: Open `api_test.html` in your browser

#### **2. Example API Calls**
```bash
# Check health
curl http://localhost:5000/health

# Get data status
curl http://localhost:5000/status/NSE_EQ

# Refresh data
curl -X POST http://localhost:5000/refresh/NSE_EQ \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2025-10-01", "end_date": "2025-11-02"}'
```

## 📁 Data Organization

```
~/NSE_BSE_Data/
├── NSE/
│   ├── EQ/          # NSE Equity data
│   ├── FO/          # NSE Futures & Options
│   ├── SME/         # NSE SME data
│   └── INDEX/       # NSE Index data
└── BSE/
    ├── EQ/          # BSE Equity data
    └── INDEX/       # BSE Index data
```

## ⚙️ Configuration

### **User Preferences**
- Stored in `~/.nse_bse_downloader/user_preferences.json`
- Automatically saved on changes
- Includes window size, download options, and append settings

### **Application Settings**
- Main configuration in `config.yaml`
- Exchange URLs and file patterns
- Default download options

## 🔧 Advanced Features

### **Data Append Operations**
- **NSE SME → NSE EQ**: Combine SME data with equity data
- **NSE INDEX → NSE EQ**: Add index data to equity files
- **BSE INDEX → BSE EQ**: Merge BSE index with equity data
- **Smart Suffix Handling**: Optional `_SME` suffix for SME symbols

### **Memory Optimization**
- Efficient DataFrame processing
- Automatic memory cleanup
- Large dataset handling

### **Error Recovery**
- Automatic retry on network failures
- Graceful handling of missing data
- Comprehensive error logging

## 🧪 Testing

### **GUI Testing**
Run the test suite to verify functionality:

```bash
# Install test dependencies
pip install pytest pytest-asyncio

# Run all tests
pytest tests/

# Run specific test
pytest tests/unit/test_config.py -v
```

### **API Testing**
Test the REST API endpoints:

```bash
# Start the API server first
python api.py

# In another terminal, run the test script
python test_api.py

# Run specific test
python test_api.py --test health

# Test with data refresh (will download data)
python test_api.py --refresh
```

Or use the interactive web interface:
```bash
# Open api_test.html in your browser
# Available at: file:///path/to/api_test.html
```

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📝 License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### **Common Issues**
- **PyQt6 Installation**: Use `pip install PyQt6` or conda equivalent
- **Network Timeouts**: Increase timeout in settings
- **Permission Errors**: Ensure write access to data directory

### **Getting Help**
- 📧 Create an issue on GitHub
- 📖 Check the documentation
- 🔍 Search existing issues

## 🏆 Acknowledgments

- NSE and BSE for providing public data access
- PyQt6 team for the excellent GUI framework
- Python community for amazing libraries

## 📊 Version History

### **v1.1.0** (2025-11-03)
- 🎉 **NEW**: Flask REST API for programmatic access
- 🌐 RESTful endpoints for data refresh and status checks
- 🎨 **NEW**: Modern Web Dashboard UI with real-time statistics
- 🚀 Beautiful, responsive browser-based interface
- 📊 Visual exchange status monitoring and batch operations
- 📋 Real-time activity log with color-coded entries
- 🧪 Interactive web-based API testing interface
- 📖 Comprehensive API and UI documentation
- 🔧 CORS support for browser-based access
- ⚡ Convenient startup scripts for API server

### **v1.0.1** (2025-08-07)       
- Enhanced download logging system
- Fixed unnecessary 'file not available' logs for current date
- Improved console output during market hours
- Better user experience with cleaner logs
       
### **bug_fixes**
- Prevented current date download attempts before 6:00 PM
- Eliminated redundant error logs in IDE console
- Fixed console spam during trading hours

### **v1.0.0** (2025-07-30)
- Initial production release
- Multi-exchange support (NSE & BSE)
- Advanced data append operations
- Professional GUI interface
- Comprehensive error handling
- Automatic update checking
- Memory optimization
- Async download processing

---

**Built with ❤️ for the trading and financial analysis community**

© 2025 Paresh Patel. All rights reserved.
