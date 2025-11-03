# 🌐 How to Access the Web UI

## ✅ Three Easy Ways

### **Method 1: Through Flask Server (BEST!)**

1. **Start the API server:**
   ```bash
   python api.py
   ```

2. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```
   or
   ```
   http://localhost:5000/
   ```

3. **Available URLs:**
   - `http://localhost:5000/` - Launcher page
   - `http://localhost:5000/dashboard` - Main dashboard
   - `http://localhost:5000/api-test` - API testing interface

**This is the recommended method!** ✨

---

### **Method 2: Direct File Access**

Simply open the HTML files directly in your browser:

**Windows:**
- Navigate to project folder in File Explorer
- Double-click `launch_ui.html`

**Full path:**
```
file:///C:/Users/panka/REPO/PYTHON/NSE_BSE_Downloader/launch_ui.html
```

---

### **Method 3: Python HTTP Server**

```bash
# In project directory
python -m http.server 8080

# Then open:
http://localhost:8080/launch_ui.html
```

---

## 🔄 After Updating api.py

**Restart the API server:**

1. Stop the current server (Ctrl+C in terminal)
2. Start it again: `python api.py`
3. Go to: `http://localhost:5000/`

---

## 📍 Quick Access URLs

| What | URL |
|------|-----|
| 🚀 **Launcher** | `http://localhost:5000/` |
| 📊 **Dashboard** | `http://localhost:5000/dashboard` |
| 🧪 **API Test** | `http://localhost:5000/api-test` |
| ❤️ **Health Check** | `http://localhost:5000/health` |
| 📈 **API Status** | `http://localhost:5000/status` |

---

## ⚠️ Troubleshooting

### "Connection Refused"
- ✅ Make sure API server is running: `python api.py`
- ✅ Check terminal for "Running on http://127.0.0.1:5000"

### "Endpoint not found"
- ✅ Restart the API server after updating api.py
- ✅ Use correct URL: `http://localhost:5000/` (not /launch_ui.html)

### "Module not found"
```bash
pip install Flask Flask-CORS pyyaml
```

---

## 🎉 Quick Start

```bash
# 1. Install dependencies
pip install Flask Flask-CORS pyyaml

# 2. Start API
python api.py

# 3. Open browser
http://localhost:5000/

# Done! 🎊
```

---

**That's it! Your web UI should now load perfectly!** ✨

