===========================================================
               EXPENSE MANAGEMENT MODULE
===========================================================

This module allows employees to submit expense claims and managers
to review, approve, or reject them. It is integrated with a custom
role-based authentication system using Django.

-----------------------------------------------------------
1. EMPLOYEE FEATURES
-----------------------------------------------------------

1. Submit Expense Claims
   - Amount
   - Category (Travel, Food, Accommodation, Office Supplies, Others)
   - Expense Date
   - Description
   - Receipt / Bill (optional upload)

2. View Expense History
   - All previously submitted expenses
   - Status shown for each:
       • Pending
       • Approved
       • Rejected

3. Track Reimbursement Status
   - Approved = Reimbursement confirmed
   - Pending = Waiting for manager review
   - Rejected = Not eligible

4. Dashboard Overview
   - Recently submitted expenses
   - Quick link to submit new expense
   - Summary of pending approvals


-----------------------------------------------------------
2. MANAGER / FINANCE FEATURES
-----------------------------------------------------------

1. View Pending Expense Claims
   - List of all employees’ submitted expenses
   - Filter by category, date, or employee (optional)
   - View full details of each claim

2. Approve or Reject Expense Claims
   - Approve with timestamp
   - Reject with manager comment (required)

3. Expense Summary Reports
   - Total expenses (all employees)
   - Category-wise distribution:
       • Travel total
       • Food total
       • Accommodation total
       • Office Supplies total
       • Others total
   - Summary appears on Manager Dashboard

4. Manager Dashboard
   - Total pending expenses
   - Today’s expense submissions
   - Quick links:
       • Pending approvals
       • Expense summary


-----------------------------------------------------------
3. DATABASE TABLES USED
-----------------------------------------------------------

A. USERS TABLE (Custom User Model)
------------------------------------
id
name
email
password
role (employee / manager)
manager_id (foreign key)

B. EXPENSE TABLE
------------------------------------
id (PK)
user_id (FK → Users)
amount (float)
category (string)
expense_date (date)
description (text)
receipt_details (string / file path)
status (Pending / Approved / Rejected)
submitted_date (timestamp)
approved_date (timestamp or null)
manager_comment (text or null)


-----------------------------------------------------------
4. EXPENSE WORKFLOW
-----------------------------------------------------------

EMPLOYEE WORKFLOW
---------------------
Step 1: Login  
Step 2: Submit new expense  
Step 3: Wait for manager approval  
Step 4: Track status in expense history  

MANAGER WORKFLOW
---------------------
Step 1: Login as manager  
Step 2: View pending claims  
Step 3: Approve or reject  
Step 4: Decision updates employee status  
Step 5: Summary reports auto-update  


-----------------------------------------------------------
5. STATUS LOGIC
-----------------------------------------------------------

PENDING:
   - Created by employee
   - Not yet reviewed by manager

APPROVED:
   - Manager accepted
   - approved_date saved
   - reimbursement considered done

REJECTED:
   - Manager denied request
   - manager_comment required


-----------------------------------------------------------
6. FILE UPLOAD HANDLING
-----------------------------------------------------------

- Employees can upload receipt images or PDFs
- Files stored in /media/receipts (configurable)
- File URL saved in receipt_details column


-----------------------------------------------------------
7. PERMISSIONS & ROLE CONTROL
-----------------------------------------------------------

EMPLOYEE CAN:
   - Create expenses
   - View only their own expenses

MANAGER CAN:
   - View all expenses
   - Approve or reject expenses
   - Access summary page


===========================================================
                 END OF EXPENSE MODULE README
===========================================================
===========================================================
               EXPENSE MANAGEMENT MODULE
===========================================================

This module allows employees to submit expense claims and managers
to review, approve, or reject them. It is integrated with a custom
role-based authentication system using Django.

-----------------------------------------------------------
1. EMPLOYEE FEATURES
-----------------------------------------------------------

1. Submit Expense Claims
   - Amount
   - Category (Travel, Food, Accommodation, Office Supplies, Others)
   - Expense Date
   - Description
   - Receipt / Bill (optional upload)

2. View Expense History
   - All previously submitted expenses
   - Status shown for each:
       • Pending
       • Approved
       • Rejected

3. Track Reimbursement Status
   - Approved = Reimbursement confirmed
   - Pending = Waiting for manager review
   - Rejected = Not eligible

4. Dashboard Overview
   - Recently submitted expenses
   - Quick link to submit new expense
   - Summary of pending approvals


-----------------------------------------------------------
2. MANAGER / FINANCE FEATURES
-----------------------------------------------------------

1. View Pending Expense Claims
   - List of all employees’ submitted expenses
   - Filter by category, date, or employee (optional)
   - View full details of each claim

2. Approve or Reject Expense Claims
   - Approve with timestamp
   - Reject with manager comment (required)

3. Expense Summary Reports
   - Total expenses (all employees)
   - Category-wise distribution:
       • Travel total
       • Food total
       • Accommodation total
       • Office Supplies total
       • Others total
   - Summary appears on Manager Dashboard

4. Manager Dashboard
   - Total pending expenses
   - Today’s expense submissions
   - Quick links:
       • Pending approvals
       • Expense summary


-----------------------------------------------------------
3. DATABASE TABLES USED
-----------------------------------------------------------

A. USERS TABLE (Custom User Model)
------------------------------------
id
name
email
password
role (employee / manager)
manager_id (foreign key)

B. EXPENSE TABLE
------------------------------------
id (PK)
user_id (FK → Users)
amount (float)
category (string)
expense_date (date)
description (text)
receipt_details (string / file path)
status (Pending / Approved / Rejected)
submitted_date (timestamp)
approved_date (timestamp or null)
manager_comment (text or null)


-----------------------------------------------------------
4. EXPENSE WORKFLOW
-----------------------------------------------------------

EMPLOYEE WORKFLOW
---------------------
Step 1: Login  
Step 2: Submit new expense  
Step 3: Wait for manager approval  
Step 4: Track status in expense history  

MANAGER WORKFLOW
---------------------
Step 1: Login as manager  
Step 2: View pending claims  
Step 3: Approve or reject  
Step 4: Decision updates employee status  
Step 5: Summary reports auto-update  


-----------------------------------------------------------
5. STATUS LOGIC
-----------------------------------------------------------

PENDING:
   - Created by employee
   - Not yet reviewed by manager

APPROVED:
   - Manager accepted
   - approved_date saved
   - reimbursement considered done

REJECTED:
   - Manager denied request
   - manager_comment required




-----------------------------------------------------------
6. PERMISSIONS & ROLE CONTROL
-----------------------------------------------------------

EMPLOYEE CAN:
   - Create expenses
   - View only their own expenses

MANAGER CAN:
   - View all expenses
   - Approve or reject expenses
   - Access summary page


===========================================================
                 END OF EXPENSE MODULE README
===========================================================
