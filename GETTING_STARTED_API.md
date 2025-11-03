# 🚀 Getting Started with Flask API

## ✨ What's New?

Your NSE/BSE Data Downloader now has a **REST API**! You can now:
- 📡 Access data programmatically via HTTP
- 🔄 Trigger downloads from any application
- 📊 Check data status remotely
- ⏰ Schedule automated refreshes
- 🔗 Integrate with other systems

---

## 📦 Installation (One-Time Setup)

### 1️⃣ Install Required Packages
```bash
pip install -r requirements.txt
```

This installs:
- ✅ Flask (web framework)
- ✅ Flask-CORS (cross-origin support)
- ✅ All existing dependencies

---

## 🎯 Quick Start Guide

### Option 1: 🖥️ Simple Startup

**Windows:**
```bash
start_api.bat
```

**Linux/Mac:**
```bash
./start_api.sh
```

The API will start at: **`http://localhost:5000`**

### Option 2: 🛠️ Manual Startup

```bash
# Basic
python api.py

# Custom port
python api.py --port 8080

# Allow external access
python api.py --host 0.0.0.0

# Debug mode
python api.py --debug
```

---

## 🧪 Test the API (Choose Your Method)

### Method 1: 🎨 **Web Interface** (Easiest!)

1. Start the API server
2. Open `api_test.html` in your browser
3. Click buttons to test different endpoints
4. See results in real-time

**Perfect for:** Quick testing, visual feedback, beginners

---

### Method 2: 🐍 **Python Test Script**

```bash
# Test all endpoints
python test_api.py

# Test specific endpoint
python test_api.py --test health

# Include data refresh tests
python test_api.py --refresh
```

**Perfect for:** Automated testing, CI/CD integration

---

### Method 3: 💻 **Command Line (cURL)**

```bash
# Health check
curl http://localhost:5000/health

# Get NSE_EQ status
curl http://localhost:5000/status/NSE_EQ

# Refresh NSE_EQ data (auto dates)
curl -X POST http://localhost:5000/refresh/NSE_EQ

# Refresh with custom dates
curl -X POST http://localhost:5000/refresh/NSE_EQ \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2025-10-01", "end_date": "2025-11-02"}'
```

**Perfect for:** Scripts, automation, cron jobs

---

### Method 4: 📮 **Postman**

1. Open Postman
2. Import `NSE_BSE_API.postman_collection.json`
3. Set base URL to `http://localhost:5000`
4. Run any request

**Perfect for:** API development, detailed testing, sharing with team

---

## 📚 API Endpoints At a Glance

| What You Want | Endpoint | Method |
|---------------|----------|--------|
| 💓 Check if API is running | `/health` | GET |
| ℹ️ Get API info | `/` | GET |
| 📊 Check all exchange status | `/status` | GET |
| 📈 Check NSE_EQ status | `/status/NSE_EQ` | GET |
| 🔄 Refresh NSE_EQ data | `/refresh/NSE_EQ` | POST |
| 🔄 Refresh all exchanges | `/refresh` | POST |
| 📋 Get data summary | `/summary` | GET |
| ⚙️ Get configuration | `/config` | GET |

---

## 💡 Common Use Cases

### 1️⃣ **Daily Automated Download**

**Linux/Mac (cron):**
```bash
# Add to crontab (crontab -e)
0 19 * * * curl -X POST http://localhost:5000/refresh
```

**Windows (Task Scheduler):**
```powershell
# Action: Start a program
# Program: curl
# Arguments: -X POST http://localhost:5000/refresh
```

---

### 2️⃣ **Check If Data Is Up-to-Date**

```python
import requests

response = requests.get('http://localhost:5000/status/NSE_EQ')
data = response.json()

if data['data']['is_up_to_date']:
    print("✅ Data is current!")
else:
    print("⚠️ Data needs update")
    # Trigger refresh
    requests.post('http://localhost:5000/refresh/NSE_EQ')
```

---

### 3️⃣ **Refresh Specific Exchanges Only**

```bash
curl -X POST http://localhost:5000/refresh \
  -H "Content-Type: application/json" \
  -d '{
    "exchanges": ["NSE_EQ", "BSE_EQ"],
    "start_date": "2025-10-01",
    "end_date": "2025-11-02"
  }'
```

---

### 4️⃣ **Integration with Trading Bot**

```python
import requests

def ensure_data_fresh():
    """Ensure data is up-to-date before trading"""
    response = requests.get('http://localhost:5000/status/NSE_EQ')
    
    if not response.json()['data']['is_up_to_date']:
        print("Refreshing data...")
        requests.post('http://localhost:5000/refresh/NSE_EQ')
        return False
    
    return True

# In your trading bot
if ensure_data_fresh():
    # Run trading strategy
    pass
```

---

## 📖 Documentation Files

| File | Purpose |
|------|---------|
| `API_README.md` | 📘 Complete API documentation |
| `API_SETUP.md` | 🔧 Setup and troubleshooting |
| `FLASK_API_SUMMARY.md` | 📝 Technical overview |
| `GETTING_STARTED_API.md` | 🚀 This quick start guide |

---

## 🎨 Visual Summary

```
┌─────────────────────────────────────────┐
│  NSE/BSE Data Downloader Flask API      │
└─────────────────────────────────────────┘
                  │
      ┌───────────┼───────────┐
      │           │           │
  ┌───▼────┐  ┌──▼───┐  ┌───▼────┐
  │  GUI   │  │ API  │  │ Cron   │
  │  App   │  │ Test │  │ Jobs   │
  └────────┘  └──────┘  └────────┘
      │           │           │
      └───────────┼───────────┘
                  │
         ┌────────▼─────────┐
         │  Data Manager    │
         └────────┬─────────┘
                  │
      ┌───────────┼───────────┐
      │           │           │
  ┌───▼───┐   ┌──▼───┐   ┌──▼───┐
  │ NSE   │   │ BSE  │   │ ...  │
  │ Files │   │Files │   │      │
  └───────┘   └──────┘   └──────┘
```

---

## ✅ Verification Checklist

After setup, verify everything works:

- [ ] API server starts without errors
- [ ] Health check returns `{"status": "healthy"}`
- [ ] Can view status of exchanges
- [ ] Web interface (`api_test.html`) works
- [ ] Test script runs successfully
- [ ] Can trigger data refresh

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: flask` | Run `pip install Flask Flask-CORS` |
| `Port 5000 in use` | Use `--port 8080` flag |
| `Connection refused` | Ensure API server is running |
| `Config not found` | Make sure `config.yaml` exists |

---

## 🎓 Next Steps

1. ✅ **Test the API**: Use `api_test.html` or `test_api.py`
2. ✅ **Read Documentation**: Check `API_README.md` for details
3. ✅ **Schedule Automation**: Set up cron/Task Scheduler
4. ✅ **Build Integrations**: Use API in your applications
5. ✅ **Deploy to Production**: Use Gunicorn for production

---

## 🎉 You're Ready!

Your NSE/BSE Data Downloader is now API-enabled!

**Start using it:**
```bash
python api.py
# Then open api_test.html in your browser
```

**Questions?** Check the detailed docs:
- 📘 `API_README.md` - Full reference
- 🔧 `API_SETUP.md` - Setup guide

---

**Built with ❤️ - Happy Trading! 📈**

