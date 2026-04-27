# AI Assistance Log
## CS665 Project 3 — Generative AI Disclosure

---

### Entry 1

**Tool:** Claude (Anthropic) — claude.ai

**Prompt:**
"I have a CS665 Project 3 assignment that requires building a full-stack Python
Flask app using my food delivery database from Project 2. Give me pin to pin
steps to build this."

**AI Output Summary:**
Claude provided a complete step-by-step guide including:
- Project folder structure
- Virtual environment setup commands
- Complete code for models.py (SQLAlchemy models for Users, Vendors, Orders)
- Complete code for app.py (Flask routes for CRUD, dashboard, transactions)
- HTML templates using Bootstrap 5 (base, index, users, vendors, orders)
- Git setup instructions
- Documentation templates for README.md and NORMALIZATION.md

**My Modifications:**
- Verified all table names and column names match my Project 2 schema exactly
- Confirmed UserID, VendorID, OrderID primary keys match previous SQL files
- Tested each route manually in the browser after pasting code
- Added my own sample data (5 users, 5 vendors, 7 orders) through the web interface
- Verified the 8% tax calculation matches the formula from my Project 2 DML file
- Confirmed the app runs correctly on my local machine at 127.0.0.1:5000
- Fixed file creation issue in PowerShell (New-Item command created wrong filenames)

---