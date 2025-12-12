# DECISIONS.md – Expense Management System

## 1. Technology Choices

### Django
I used Django because:
- I have prior internship experience with Django
- Its ORM simplifies working with structured financial data
- Built-in user authentication supports role-based access

### PostgreSQL
Used for consistency across both projects.
Benefits:
- ACID compliance (important for financial records)
- Easy cloud hosting on Render
- Good performance with structured models

### Bootstrap UI
Kept UI simple because the focus is functionality:
- Expense submission
- Receipt upload
- Manager approval

### Deployment: Render
Render was chosen because:
- Easy PostgreSQL integration
- Automatic CI/CD from GitHub
- Free tier support

---

## 2. Implementation Decisions

### Database Schema
I structured the DB around:
- **User**
- **Expense** (amount, category, description, receipt image)
- **Approval workflow** (status + manager comments)

### Assumptions
- Only employees submit expenses
- Only managers/finance can approve
- No multi-level approval required

### Features Prioritized
- Submit and track expenses
- Manager dashboard for approval
- Receipt upload system
- Status tracking

---

## 3. Challenges

### 1. Multiple DB URL Issues
I faced:
- Wrong Render hostname
- Password authentication failures
- Missing .env values
These were fixed by correcting:
- DATABASE_URL formatting
- dotenv loading
- Render environment variables

### 2. Static Files & Deployment
- Collectstatic failed initially
- Whitenoise configuration needed fixes

### 3. Adding Manager Features
New features required updating:
- Views
- Templates
- Manager dashboard logic

---

## 4. Improvements with More Time
- Add receipt compression + size validation
- Add PDF/CSV export of expenses
- Add analytics dashboard
- Add email/SMS notifications

---

## 5. Trade-offs & Shortcuts
- UI is basic due to time limit
- No detailed finance reporting system included
- No multi-role finance hierarchy


