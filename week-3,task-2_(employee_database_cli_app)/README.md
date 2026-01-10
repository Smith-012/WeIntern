# Employee Management CLI Application

This project is a **Python-based Employee Management System** using
SQLite, featuring:

-   CRUD operations (Create, Read, Update, Delete)
-   Live input validation (only alphabets for names/departments, only
    numbers for age/ID)
-   Cross‑platform key capture for restricted typing
-   Auto‑database migration
-   Colorful interactive terminal UI
-   Clear screen functionality
-   Stored date (YYYY‑MM‑DD)

------------------------------------------------------------------------

## 📌 How It Works

### ✔ Main Features:

  -----------------------------------------------------------------------
  Feature                     Description
  --------------------------- -------------------------------------------
  Add Employee                Stores new employee with name, age,
                              department, and auto-date.

  View Employees              Displays all records in formatted table.

  Update Employee             Edits existing employee & shows updated
                              record.

  Delete Employee             Deletes an employee by ID.

  Clear Screen                Clears terminal window.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🧠 Main Brain Logic

### ⭐ CRUD Operations

CRUD operations are handled inside the `EmployeeManager` class:

-   **Create** → `add_employee()`
-   **Read** → `get_all()` + `get_employee()`
-   **Update** → `update_employee()`
-   **Delete** → `delete_employee()`

SQLite is used for storage.\
Database auto‑creates if missing.

### ⭐ Live Input Validation

**input_alpha()**\
Allows: - A--Z\
- a--z\
- spaces ONLY

**input_number()**\
Allows: - digits 0--9 ONLY

Everything else is ignored *live*, not even shown on screen.

### ⭐ Auto Migration

Old databases missing `stored_at` column get upgraded automatically.

### ⭐ Stored Date

Stored using:

    DATE('now')

So only the date (no time) is saved.

------------------------------------------------------------------------

## ▶️ How to Run This Program

### **1. Install Python 3**

Make sure Python 3 is installed.

### **2. Install Dependencies**

    pip install colorama

### **3. Save the Program**

Save your `.py` file (example: `employee_manager.py`).

### **4. Run the Program**

    python employee_manager.py

------------------------------------------------------------------------

## 🖼 Example Output

### **Main Menu**

    ======= Employee Database CLI =======
    1. Add Employee
    2. View Employees
    3. Update Employee
    4. Delete Employee
    5. Clear Screen
    6. Exit

------------------------------------------------------------------------

### ✅ **Add Employee Example**

    Name: John Doe
    Age: 29
    Department: HR

    ✔ Employee added successfully!
    Stored Record:
    ID: 12
    Name: John Doe
    Age: 29
    Department: HR
    Stored At: 2026-01-12

------------------------------------------------------------------------

### 📄 **View Employees Example**

    ---- Employee List ----
    ID    NAME            AGE   DEPT            DATE STORED
    --------------------------------------------------------
    1     John Doe        29    HR              2026-01-12
    2     Alice Smith     25    Sales           2026-01-12

------------------------------------------------------------------------

### ✏️ **Update Example**

    Employee ID: 1
    New Name: John X Doe
    New Age: 30
    New Department: HR

    ✔ Employee updated!
    Updated Record:
    ID: 1
    Name: John X Doe
    Age: 30
    Department: HR
    Stored At: 2026-01-12

------------------------------------------------------------------------

### ❌ **Delete Example**

    Employee ID: 5
    ✔ Employee deleted!

------------------------------------------------------------------------

### 🧹 **Clear Screen Example**

Just clears the terminal screen.

------------------------------------------------------------------------

## 📄 File Maintainer

-   Author: Your Name\
-   Language: Python\
-   Database: SQLite\
-   Terminal UI: Colorama

------------------------------------------------------------------------

## ✔️ License

This project is free to use, modify, and distribute.
