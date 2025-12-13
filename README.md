EXPENSE MANAGEMENT SYSTEM

Project Description
The Expense Management System allows employees to submit expense claims and track their status.
Managers can review pending claims, approve or reject them, and view expense summaries.
The system ensures role-based access and a smooth approval workflow.

Technology Stack
Backend: Django (Python)
Frontend: Django Templates, Bootstrap
Database: PostgreSQL (Production), SQLite (Local)
Authentication: Django Custom User Model
Deployment: Render

Database Setup Instructions
The project uses PostgreSQL in production via DATABASE_URL.
For local development, SQLite is used by default.

To use PostgreSQL locally:
1. Create a PostgreSQL database
2. Set DATABASE_URL in .env file
3. Run migrations

Step-by-Step Instructions to Run Locally
1. Clone the repository
2. Create and activate virtual environment
3. Install dependencies:
   pip install -r requirements.txt
4. Create .env file with:
   SECRET_KEY
   DEBUG=True
   DATABASE_URL (optional)
5. Run migrations:
   python manage.py migrate
6. Create superuser:
   python manage.py createsuperuser
7. Run server:
   python manage.py runserver
8. Open http://127.0.0.1:8000

Deployed Application URL
https://expense-management1.onrender.com

Test Credentials
Employee:
Username: vishwa
Password:basu1234

Manager:
Username: basu
Password: basu123

Known Limitations
• No file upload for receipts (text only)
• Basic reports (no CSV export)
• UI kept simple due to time constraints
