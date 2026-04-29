# Use of AI
## CS665 Project 3 — Generative AI Disclosure

---

### Overview

For this project, Claude (Anthropic) was used as a coding and learning assistant.
The goal was to use AI the same way a developer would use documentation or Stack
Overflow — to understand concepts, get unstuck, and verify thinking. No output
was blindly copied. Every suggestion was read, understood, and tested before
being included in the project.

---

### 1. Understanding Flask Project Structure

**Tool:** Claude (Anthropic) — claude.ai

**Purpose:**
Coming from a SQL and database background, the structure of a Flask project was
unfamiliar. Claude was used to understand how Flask connects to a database using
SQLAlchemy, and how routes, models, and templates work together as a system.

**Key concepts learned:**
- SQLAlchemy models map directly to database tables
- Flask routes handle GET and POST HTTP requests
- Jinja2 templates receive Python data and render it dynamically in HTML

**Personal contribution:**
The Flask models were mapped directly to the existing Project 2 schema — the
same Users, Vendors, and Orders tables already designed. Every column name,
data type, and foreign key was matched exactly to the original database design.
The database design itself was not AI generated — it was a personal design from
Project 2, translated into Python classes.

---

### 2. Writing the Application Code

**Tool:** Claude (Anthropic) — claude.ai

**Purpose:**
Claude was used to help write Flask routes for CRUD operations. The request was
specific — describing the exact tables, the project requirements, and the
features needed: multi-table CRUD, transaction logic, server-side validation,
and a summary dashboard using SQL aggregate functions.

**How the output was verified:**
- Every route was tested manually by navigating through the browser
- The transaction logic (creating an order and calculating 8% tax in a single
  commit) was traced through the code to confirm it matched the Project 2
  DML formula exactly
- Server-side validation was tested by deliberately submitting empty forms and
  negative prices to confirm errors were caught correctly
- Dashboard COUNT, SUM, and AVG values were cross-checked against actual
  data entered into the system

**Personal contribution:**
All sample data was added manually through the web interface — 5 users,
5 vendors, and 7 orders — using the same names and values from the Project 2
dataset. This allowed personal end-to-end verification of every feature.

---

### 3. Frontend and Template Design

**Tool:** Claude (Anthropic) — claude.ai

**Purpose:**
Claude was used to help structure HTML templates using Bootstrap 5, including
a navbar, modal popups for add and edit forms, and a dashboard with stat cards
displaying live database numbers.

**Personal contribution:**
The layout choices, color decisions, and which metrics to highlight on the
dashboard were independent decisions. Total Users, Total Orders, Total Revenue,
and Average Order Value were chosen because they are the most meaningful metrics
for a food delivery business context — not because they were suggested by AI.

---

### 4. Normalization Report

**Tool:** Claude (Anthropic) — claude.ai

**Purpose:**
The schema was already known to be in 3NF from Project 2 design work. Claude
was used to help articulate and document the reasoning formally, since writing
a normalization report in academic language was a new type of deliverable.

**How the output was verified:**
- Every functional dependency listed was confirmed against the actual table columns
- The 3NF conclusion was verified by checking that no non-key attribute determines
  another non-key attribute in any of the three tables
- The final relational schema in the report was confirmed to match models.py exactly

---

### 5. Debugging and Problem Solving

**Tool:** Claude (Anthropic) — claude.ai

**Purpose:**
Several real-world errors came up during development. Screenshots of errors were
shared with Claude to work through fixes collaboratively.

**Issues resolved:**
- PowerShell's New-Item command was creating files with the full command as the
  filename. Claude identified this from a directory listing screenshot and
  suggested the correct echo redirect syntax.
- Git was initialized in the wrong directory. Claude identified this from the
  terminal prompt path and explained the importance of directory context in Git.
- GitHub push authentication required a Personal Access Token. Claude explained
  why GitHub deprecated password authentication and walked through generating
  a token with the correct repo scope.

**What was gained:**
These debugging sessions built real understanding of PowerShell vs CMD differences,
Git directory management, and GitHub authentication — practical knowledge that
extends beyond this project.

---

### Reflection

AI was used as a productivity tool, not a replacement for understanding. When
errors occurred, they had to be read carefully, described clearly, and the
suggested fixes had to be evaluated before applying them. The debugging portions
of this project required the most genuine engagement with the code — because
they could not be solved without understanding what was actually happening.

