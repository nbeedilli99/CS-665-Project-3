# AI Assistance Log
## CS665 Project 3 — Generative AI Disclosure

---

### Overview

For this project, I used Claude (Anthropic) as a learning and coding assistant.
My approach was to use AI the same way a developer would use documentation or
Stack Overflow — to understand concepts, get unstuck, and verify my thinking.
I did not blindly copy output. Every suggestion was read, understood, and tested
before being included in the project.

---

### Entry 1 — Understanding Flask Project Structure

**Tool:** Claude (Anthropic) — claude.ai

**How I used it:**
Coming from a SQL/database background, I was unfamiliar with how Flask projects
are organized. I asked Claude to explain how a Flask app connects to a database
using SQLAlchemy, and how routes, models, and templates work together.

**What I learned:**
- How SQLAlchemy models map directly to database tables
- How Flask routes handle GET and POST requests
- How Jinja2 templates receive data from Python and render it in HTML

**What I did myself:**
I mapped the Flask models directly to my own Project 2 schema — the same
Users, Vendors, and Orders tables I had already designed. I made sure every
column name, data type, and foreign key matched exactly what I had built before.
This was not AI's database design — it was mine, translated into Python classes.

---

### Entry 2 — Writing the Application Code

**Tool:** Claude (Anthropic) — claude.ai

**How I used it:**
I asked Claude to help me write the Flask routes for CRUD operations. Rather than
asking for a generic app, I described my specific tables and requirements from
the project brief — multi-table CRUD, transaction logic, server-side validation,
and a summary dashboard using SQL aggregates.

**What I verified:**
- Every route was tested manually by clicking through the browser
- The transaction logic (creating an order + calculating 8% tax in one commit)
  was traced through the code to confirm it matched my Project 2 DML formula
- Server-side validation was tested by deliberately submitting empty forms and
  negative prices to confirm errors were caught correctly
- The dashboard COUNT, SUM, and AVG values were cross-checked against the
  actual data I had entered

**What I did myself:**
I added all sample data manually through the web interface — 5 users, 5 vendors,
and 7 orders — using the same names and values from my Project 2 dataset.
This let me personally verify that every feature worked end to end.

---

### Entry 3 — Frontend Design Decisions

**Tool:** Claude (Anthropic) — claude.ai

**How I used it:**
I asked Claude to help structure the HTML templates using Bootstrap 5. I specified
that I wanted a navbar, modal popups for forms, and a dashboard with stat cards
showing live database numbers.

**What I decided myself:**
The color scheme, layout choices, and which information to highlight on the
dashboard were my own decisions. I chose to display Total Users, Total Orders,
Total Revenue, and Average Order Value because these are the metrics that make
sense for a food delivery business — not because AI suggested them.

---

### Entry 4 — Normalization Report

**Tool:** Claude (Anthropic) — claude.ai

**How I used it:**
I already knew from class that my schema was in 3NF — I had designed it carefully
in Project 2. I used Claude to help me articulate and document the reasoning
formally, since writing a normalization report in academic language was new to me.

**What I verified:**
- I read every functional dependency listed and confirmed each one against my
  actual table columns
- I verified the 3NF conclusion by checking that no non-key attribute determines
  another non-key attribute in any of my three tables
- The final relational schema in the report matches models.py exactly

---

### Entry 5 — Debugging & Problem Solving

**Tool:** Claude (Anthropic) — claude.ai

**How I used it:**
During development I ran into several real-world errors that I had not seen before.
I shared screenshots of the errors with Claude and worked through the fixes.

**Problems solved:**
- PowerShell's New-Item command was creating files with the full command as the
  filename instead of just the filename. Claude identified this immediately from
  the directory listing screenshot.
- Git was initialized in the wrong directory. Claude spotted this from the prompt
  path and explained why it matters.
- GitHub push authentication required a Personal Access Token instead of a
  password. Claude explained why GitHub changed this policy and walked me through
  generating one.

**What I learned:**
These debugging sessions taught me more than the happy path would have. I now
understand PowerShell vs CMD differences, how Git tracks directories, and how
GitHub authentication works — knowledge I will carry into future projects.

---

### Honest Reflection

Using AI for this project felt similar to pair programming with a senior developer.
It accelerated my productivity significantly, but the understanding had to come
from me. When something did not work, I had to read the error, describe it
clearly, and evaluate whether the suggested fix made sense before applying it.

The parts of this project I am most confident about are the ones where something
went wrong and I had to debug it — because those required me to genuinely
understand what the code was doing, not just copy it.

**Repository:** https://github.com/nbeedilli99/CS-665-Project-3