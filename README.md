# Expense Management System

A Django web application that allows employees to submit expenses and managers/finance teams to approve or reject them. Useful for tracking reimbursements within an organization.

---

## 🚀 Features

### For Employees
- Submit expense claims (amount, description, receipt upload)
- View expense history
- Track approval status

### For Managers / Finance
- View pending expense claims
- Approve or reject expenses
- Add comments for decisions
- View expense summaries

---

## 🛠 Technology Stack

- **Backend:** Django 6
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** PostgreSQL (Render Cloud)
- **File Storage:** Local (staticfiles)
- **Deployment:** Render

---

# Step-by-Step Instructions to Run the Project Locally

## 1. Clone the Repository
git clone https://github.com/Basavaraj607/Expense_Management1
cd company
## 2. Create Virtual Environment
python -m venv env
env\Scripts\activate   (Windows)
source env/bin/activate (Mac/Linux)

## 3. Install Dependencies
pip install -r requirements.txt

## 4. Create .env File
In the project root, add a file named `.env`:

SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3

(Use the PostgreSQL URL only for deployment, not local.)


----------------------------------------------------------------------
TEST LOGIN CREDENTIALS
----------------------------------------------------------------------

ADMIN / MANAGER LOGIN:
username: basu
password: basu123

EMPLOYEE LOGIN:
username: vishwa
password: basu1234


## 5. Apply Migrations
python manage.py migrate

## 6. Create Superuser (for login)
python manage.py createsuperuser

Enter username, email and password.

## 7. Run the Development Server
python manage.py runserver

Server will start at:
http://127.0.0.1:8000/

## 8. Login
Use your superuser credentials or test accounts (if provided in README).

## 9. Stop Server
Press CTRL + C in terminal to stop the server.
