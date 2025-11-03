# 🎨 Web UI Guide - NSE/BSE Data Downloader

## Overview

The Web UI provides a modern, intuitive dashboard for managing your NSE/BSE market data through a browser interface.

---

## 🚀 Quick Start

### Method 1: Using the Launcher (Recommended)

1. **Start the API server:**
   ```bash
   python api.py
   ```

2. **Open the launcher:**
   - Double-click `launch_ui.html` or
   - Open it in your browser: `file:///path/to/launch_ui.html`

3. **Click "Launch Dashboard"** when the API shows as online

### Method 2: Direct Access

1. Start the API server: `python api.py`
2. Open `web_ui.html` directly in your browser

---

## 📋 UI Features

### 1. **Dashboard Header**

![Header Section]

**Features:**
- **API Status Indicator**: Shows real-time connection status
  - 🟢 Green dot = API Online
  - 🔴 Red dot = API Offline
- **API URL Configuration**: Change API endpoint if needed
- **Reconnect Button**: Manually check API connection

---

### 2. **Statistics Dashboard**

Four key metrics displayed at a glance:

| Metric | Description |
|--------|-------------|
| 📈 **Total Exchanges** | Number of available exchanges (NSE/BSE) |
| ✅ **Active Data** | Exchanges with data files |
| 📁 **Total Files** | Total number of data files stored |
| 🕐 **Last Updated** | Most recent data date |

---

### 3. **Exchange Status Panel**

**Features:**
- **Visual Status Indicators:**
  - 🟢 `UP-TO-DATE` - Data is current
  - 🟡 `NEEDS UPDATE` - Data requires refresh
  - 🔴 `NO DATA` - No data files exist

- **Exchange Information:**
  - Last data date
  - Number of files
  - First run status

- **Selection Tools:**
  - Click any exchange card to select/deselect
  - "Select All" button
  - "Deselect All" button
  - "Refresh Status" button

**Color Coding:**
- Selected exchanges have a blue border and background
- Unselected exchanges have a gray border

---

### 4. **Activity Log**

Real-time activity tracking with:
- ⏰ **Timestamps** for each action
- 🎨 **Color-coded entries:**
  - Blue = Informational
  - Green = Success
  - Red = Error
- 📜 **Auto-scroll** for latest entries
- 🗑️ **Clear Log** button

---

### 5. **Actions Panel**

**Date Range Selection (Optional):**
- Start Date: Beginning of date range
- End Date: End of date range
- Leave empty for automatic date calculation

**Action Buttons:**
- 🔄 **Refresh Selected Exchanges**: Updates only selected exchanges
  - Shows count of selected exchanges
  - Disabled if no exchanges selected
- ⚡ **Refresh All Exchanges**: Updates all available exchanges
  - Requires confirmation
  - Automatically selects all exchanges

---

### 6. **Progress Modal**

During data refresh operations:
- **Progress Bar**: Visual indication of completion
- **Exchange Results**: Shows success/failure for each exchange
- **Details Display:**
  - ✅ Success with green background
  - ❌ Failure with red background
  - Number of dates processed
  - Error messages if applicable
- **Auto-close**: Closes after 5 seconds upon completion

---

## 🎯 Common Workflows

### Workflow 1: Check Data Status

```
1. Open Web UI
2. View Dashboard Statistics
3. Check Exchange Status Panel
4. Look for status badges:
   - UP-TO-DATE = Good to go
   - NEEDS UPDATE = Action required
```

### Workflow 2: Refresh Specific Exchanges

```
1. Click on exchange cards to select them
2. Optionally set date range
3. Click "Refresh Selected Exchanges"
4. Monitor progress in modal
5. Check Activity Log for results
```

### Workflow 3: Full Data Update

```
1. Click "Refresh All Exchanges"
2. Confirm the action
3. Wait for completion
4. Check updated statistics
```

### Workflow 4: Historical Data Download

```
1. Select desired exchanges
2. Set Start Date (e.g., 2025-01-01)
3. Set End Date (e.g., 2025-10-31)
4. Click "Refresh Selected Exchanges"
5. Monitor progress
```

---

## 🎨 UI Components

### Color Scheme

| Color | Usage | Hex Code |
|-------|-------|----------|
| Primary | Main brand color | #667eea |
| Secondary | Accent color | #764ba2 |
| Success | Positive actions | #48bb78 |
| Warning | Caution items | #ed8936 |
| Error | Failures | #f56565 |
| Info | Information | #4299e1 |

### Typography

- **Headers**: Segoe UI, 2.5em bold
- **Body**: Segoe UI, 1em regular
- **Monospace**: Courier New (for dates/codes)

### Layout

- **Responsive Grid**: Adapts to screen size
- **Cards**: Rounded corners (12px radius)
- **Spacing**: Consistent 20px gaps
- **Shadows**: Subtle elevation effects

---

## 💡 Tips & Tricks

### 1. **Auto-Refresh**
- Statistics update every 30 seconds automatically
- No need to manually refresh for status updates

### 2. **Keyboard Shortcuts**
- `Ctrl+R` / `Cmd+R`: Reload page
- `F12`: Open browser developer tools for debugging

### 3. **Multiple Windows**
- Open multiple dashboard windows for monitoring
- Each window operates independently

### 4. **Mobile Access**
- Fully responsive design
- Access from tablets and phones
- Touch-friendly interface

### 5. **API URL Flexibility**
- Change API URL for remote access
- Save custom URL in browser
- Useful for multi-machine setups

---

## 🔧 Configuration

### Changing API URL

If your API is running on a different port or machine:

1. Click the API URL input in header
2. Enter new URL (e.g., `http://192.168.1.100:8080`)
3. Click "Reconnect"
4. Wait for green status indicator

### Browser Requirements

**Recommended Browsers:**
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Edge 90+
- ✅ Safari 14+

**Required Features:**
- JavaScript enabled
- Fetch API support
- CSS Grid support
- Local Storage (optional)

---

## 🐛 Troubleshooting

### Issue: "API Offline" Status

**Solutions:**
1. Verify API server is running: `python api.py`
2. Check API URL is correct
3. Try reconnecting
4. Check firewall settings
5. Verify port 5000 is not blocked

### Issue: Exchanges Not Loading

**Solutions:**
1. Check browser console (F12) for errors
2. Verify API health endpoint works
3. Clear browser cache
4. Reload the page

### Issue: Progress Modal Stuck

**Solutions:**
1. Check Activity Log for errors
2. Verify network connectivity
3. Close and retry operation
4. Check API logs for issues

### Issue: Selection Not Working

**Solutions:**
1. Ensure exchanges are loaded
2. Try "Select All" button first
3. Refresh exchange status
4. Reload the page

---

## 📊 Understanding the Data

### Exchange Codes

| Code | Full Name |
|------|-----------|
| NSE_EQ | NSE Equity |
| NSE_FO | NSE Futures & Options |
| NSE_SME | NSE Small & Medium Enterprises |
| NSE_INDEX | NSE Indices |
| BSE_EQ | BSE Equity |
| BSE_INDEX | BSE Indices |

### Status Badges

- **UP-TO-DATE**: Last file date is within 3 days
- **NEEDS UPDATE**: Last file date is older than 3 days
- **NO DATA**: No data files exist for this exchange

### Date Handling

- Dates use YYYY-MM-DD format
- Weekends are automatically skipped
- Market holidays are excluded
- Current day excluded if before 6 PM

---

## 🎓 Advanced Usage

### 1. **Batch Operations**

Select multiple exchanges and refresh them together:
```
1. Select: NSE_EQ, NSE_FO, NSE_INDEX
2. Set date range if needed
3. Refresh Selected
4. All three update simultaneously
```

### 2. **Regular Monitoring**

Keep the dashboard open:
- Stats auto-update every 30 seconds
- Activity log shows real-time events
- Status indicators reflect current state

### 3. **Historical Data Collection**

Download data for specific periods:
```
1. Select exchanges
2. Start Date: 2024-01-01
3. End Date: 2024-12-31
4. Refresh - downloads entire year
```

### 4. **Integration with Workflows**

Use the UI alongside other tools:
- Monitor status while running scripts
- Verify data after automated jobs
- Quick manual fixes when needed

---

## 🎉 UI Highlights

### Modern Design
- Gradient backgrounds
- Smooth animations
- Hover effects
- Responsive layout

### User Experience
- Intuitive navigation
- Clear visual feedback
- Helpful error messages
- Progress indication

### Performance
- Fast page loads
- Efficient updates
- Minimal data transfer
- Browser caching

---

## 📝 Changelog

### Version 1.1.0 (Current)
- ✨ Initial release of Web UI
- 📊 Dashboard with statistics
- 📈 Exchange status panel
- 📋 Activity log
- ⚡ Batch refresh operations
- 🎨 Modern, responsive design

---

## 🆘 Getting Help

**If you encounter issues:**

1. Check the Activity Log for error messages
2. Review API logs: Check terminal where `api.py` is running
3. Browser Console: Press F12 and check for JavaScript errors
4. API Health: Test `http://localhost:5000/health` directly
5. Documentation: See `API_README.md` for API details

**Common Solutions:**
- Restart API server
- Reload web page
- Clear browser cache
- Check network connectivity

---

## 🔮 Future Enhancements

Planned features for upcoming versions:
- 📊 Charts and graphs
- 📈 Data visualization
- 🔔 Browser notifications
- 💾 Download history
- ⚙️ User preferences
- 🌙 Dark mode
- 📱 Progressive Web App (PWA)
- 🔄 Real-time WebSocket updates

---

## ✨ Summary

The Web UI provides:
- ✅ Modern, intuitive interface
- ✅ Real-time status monitoring
- ✅ Easy data refresh operations
- ✅ Comprehensive activity logging
- ✅ Responsive, mobile-friendly design
- ✅ No installation required (just a browser!)

**Start using it now:**
```bash
python api.py          # Start API
open launch_ui.html    # Launch UI
```

---

**Enjoy your new Web Dashboard! 🚀**

