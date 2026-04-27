# AI Assistance Log
## CS665 Project 3 — Generative AI Disclosure

---

### Entry 1 — Project Planning & Setup

**Tool:** Claude (Anthropic) — claude.ai (Claude Sonnet 4.5)

**Date:** April 27, 2026

**Prompt:**
"I have a CS665 Project 3 assignment that requires building a full-stack Python
Flask app using my food delivery database from Project 2. Give me pin to pin
steps to build this."

**AI Output Summary:**
Claude provided a complete step-by-step guide including:
- Project folder structure recommendation
- Virtual environment setup commands for Windows
- Complete code for models.py (SQLAlchemy models for Users, Vendors, Orders)
- Complete code for app.py (Flask routes for CRUD, dashboard, transactions)
- HTML templates using Bootstrap 5 (base.html, index.html, users.html, vendors.html, orders.html)
- Git setup and GitHub push instructions
- Content for README.md, NORMALIZATION.md, and AI_LOG.md

**My Modifications & Verification:**
- Verified all table names (users, vendors, orders) match my Project 2 schema exactly
- Confirmed primary keys (UserID, VendorID, OrderID) match my previous SQL files
- Tested every route manually in the browser: dashboard, /users, /vendors, /orders
- Added my own real sample data: 5 users, 5 vendors, 7 orders through the web UI
- Verified the 8% tax calculation (SubTotal * 1.08) matches my Project 2 DML formula
- Debugged and fixed a PowerShell file creation issue (New-Item created wrong filenames)
- Debugged git init running in wrong directory and fixed by navigating to correct folder
- Confirmed the app runs correctly at http://127.0.0.1:5000

---

### Entry 2 — Normalization Report

**Tool:** Claude (Anthropic) — claude.ai

**Date:** April 27, 2026

**Prompt:**
"Help me write the NORMALIZATION.md report for my database. My schema has
Users, Vendors, and Orders tables."

**AI Output Summary:**
Claude generated the full normalization report including functional dependencies,
anomaly identification, 1NF/2NF/3NF analysis, and final relational schema.

**My Modifications & Verification:**
- Reviewed every functional dependency listed and confirmed it matches my actual schema
- Verified the 3NF conclusion is correct — no transitive dependencies exist in my tables
- Confirmed the final relational schema section matches the exact models in models.py
- The analysis correctly explains why no decomposition was needed

---

### Entry 3 — Debugging Assistance

**Tool:** Claude (Anthropic) — claude.ai

**Date:** April 27, 2026

**Prompt:**
Multiple debugging sessions throughout development including:
- PowerShell file creation errors (New-Item creating wrong filenames)
- Git init running in wrong directory
- Git push authentication issues

**AI Output Summary:**
Claude diagnosed each error from screenshots and provided corrected commands.

**My Modifications & Verification:**
- Executed each suggested fix and verified it resolved the issue
- Learned the difference between PowerShell and CMD syntax
- Successfully pushed all code to GitHub after following corrected git commands
- Final repository at: https://github.com/nbeedilli99/CS-665-Project-3

---

### Summary of AI Usage

| Area | AI Used | My Contribution |
|------|---------|-----------------|
| App architecture | Yes | Verified against Project 2 schema |
| Python/Flask code | Yes | Tested all routes manually |
| HTML templates | Yes | Verified rendering in browser |
| Sample data | No | Added manually through the UI |
| Debugging | Yes | Identified errors, applied fixes |
| Normalization analysis | Yes | Verified all logic is correct |
| Git/GitHub setup | Yes | Executed and verified all steps |

**Total AI assistance level: High — all code was AI-assisted but personally
verified, tested, and understood before submission.**