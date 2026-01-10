# Employee Management CLI Application

This project is a **Python-based Employee Management System** using
SQLite, featuring:

-   CRUD operations (Create, Read, Update, Delete)
-   Live input validation
-   Cross‑platform key capture for restricted typing
-   Auto‑database migration
-   Colorful interactive terminal UI
-   Clear screen functionality
-   Stored date (YYYY‑MM‑DD)

------------------------------------------------------------------------
## 📌 How It Works

| Operations           | Description |
|-------------------|-------------|
| **Add Employee**  | Stores a new employee with name, age, department, and auto-date. |
| **View Employees** | Displays all records in a formatted table. |
| **Update Employee** | Edits an existing employee and shows the updated record. |
| **Delete Employee** | Deletes an employee by ID. |
| **Clear Screen** | Clears the terminal window. |
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

    Name: Raju
    Age: 25
    Department: IT

    ✔ Employee added successfully!
    Stored Record:
    ID: 1
    Name: Raju
    Age: 25
    Department: IT
    Stored At: 2026-01-06

------------------------------------------------------------------------

### 📄 **View Employees Example**

    ---- Employee List ----
    ID    NAME            AGE   DEPT            DATE STORED
    --------------------------------------------------------
    1     Raju            25    IT              2026-01-06

------------------------------------------------------------------------

### ✏️ **Update Example**

    Employee ID: 1
    New Name: Raju
    New Age: 27
    New Department: IT

    ✔ Employee updated!
    Updated Record:
    ID: 1
    Name: Raju
    Age: 27
    Department: IT
    Stored At: 2026-01-06

------------------------------------------------------------------------

### ❌ **Delete Example**

    Employee ID: 5
    ✔ Employee deleted!

------------------------------------------------------------------------

### 🧹 **Clear Screen Example**

Just clears the terminal screen.

------------------------------------------------------------------------
