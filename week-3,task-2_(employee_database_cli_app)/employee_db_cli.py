import sqlite3
import sys
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

DB_NAME = "employees.db"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

if os.name == "nt":
    import msvcrt

    def getch():
        return msvcrt.getwch()

else:
    import tty
    import termios

    def getch():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return ch

def input_alpha(prompt):
    print(Fore.MAGENTA + prompt, end="", flush=True)
    text = ""
    while True:
        ch = getch()

        if ch in ["\r", "\n"]:
            print()
            return text.strip()

        if ch in ["\x08", "\x7f"]:  
            if len(text) > 0:
                text = text[:-1]
                print("\b \b", end="", flush=True)
            continue

        if ch.isalpha() or ch == " ":
            text += ch
            print(ch, end="", flush=True)
            
def input_number(prompt):
    print(Fore.MAGENTA + prompt, end="", flush=True)
    text = ""
    while True:
        ch = getch()

        if ch in ["\r", "\n"]:
            print()
            return text.strip()

        if ch in ["\x08", "\x7f"]:
            if len(text) > 0:
                text = text[:-1]
                print("\b \b", end="", flush=True)
            continue

        if ch.isdigit():
            text += ch
            print(ch, end="", flush=True)

class EmployeeManager:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self.create_table()
        self.migrate_database()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employees(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                department TEXT
            )
        """)
        conn.commit()
        conn.close()

    def migrate_database(self):
        conn = self.connect()
        cur = conn.cursor()

        cur.execute("PRAGMA table_info(employees)")
        columns = [c[1] for c in cur.fetchall()]

        if "stored_at" not in columns:
            print(Fore.YELLOW + "⚠ Updating old database: Adding 'stored_at' column...")
            cur.execute("ALTER TABLE employees ADD COLUMN stored_at TEXT DEFAULT (DATE('now'))")
            conn.commit()

        conn.close()

    def employee_exists(self, emp_id):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT id FROM employees WHERE id = ?", (emp_id,))
        result = cur.fetchone()
        conn.close()
        return result is not None

    def get_employee(self, emp_id):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT id, name, age, department, stored_at FROM employees WHERE id = ?", (emp_id,))
        result = cur.fetchone()
        conn.close()
        return result

    def add_employee(self, name, age, dept):
        conn = self.connect()
        cur = conn.cursor()

        cur.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)",
                    (name, age, dept))

        emp_id = cur.lastrowid

        cur.execute("SELECT stored_at FROM employees WHERE id = ?", (emp_id,))
        stored_at = cur.fetchone()[0]

        conn.commit()
        conn.close()
        return emp_id, stored_at

    def get_all(self):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT id, name, age, department, stored_at FROM employees")
        rows = cur.fetchall()
        conn.close()
        return rows

    def update_employee(self, emp_id, name, age, dept):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("UPDATE employees SET name = ?, age = ?, department = ? WHERE id = ?",
                    (name, age, dept, emp_id))
        updated = cur.rowcount
        conn.commit()
        conn.close()
        return updated > 0

    def delete_employee(self, emp_id):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
        deleted = cur.rowcount
        conn.commit()
        conn.close()
        return deleted > 0

def print_menu():
    print(Fore.CYAN + "\n======= Employee Database CLI =======")
    print(Fore.YELLOW + "1." + Fore.WHITE + " Add Employee")
    print(Fore.YELLOW + "2." + Fore.WHITE + " View Employees")
    print(Fore.YELLOW + "3." + Fore.WHITE + " Update Employee")
    print(Fore.YELLOW + "4." + Fore.WHITE + " Delete Employee")
    print(Fore.YELLOW + "5." + Fore.WHITE + " Clear Screen")
    print(Fore.YELLOW + "6." + Fore.RED + " Exit")

def main():
    manager = EmployeeManager()

    while True:
        print_menu()
        choice = input(Fore.GREEN + "\nEnter choice: ")

        if choice == "1":
            name = input_alpha("Name: ")
            age = int(input_number("Age: "))
            dept = input_alpha("Department: ")

            emp_id, stored_at = manager.add_employee(name, age, dept)

            print(Fore.GREEN + "\n✔ Employee added successfully!")
            print(Fore.CYAN + "Stored Record:")
            print(f"{Fore.YELLOW}ID: {Fore.WHITE}{emp_id}")
            print(f"{Fore.YELLOW}Name: {Fore.WHITE}{name}")
            print(f"{Fore.YELLOW}Age: {Fore.WHITE}{age}")
            print(f"{Fore.YELLOW}Department: {Fore.WHITE}{dept}")
            print(f"{Fore.YELLOW}Stored At: {Fore.WHITE}{stored_at}\n")
        elif choice == "2":
            rows = manager.get_all()

            if not rows:
                print(Fore.RED + "No employees found.\n")
            else:
                print(Fore.CYAN + "\n---- Employee List ----")
                print(f"{'ID':<5} {'NAME':<15} {'AGE':<5} {'DEPT':<15} {'DATE STORED'}")
                print("-" * 70)

                for r in rows:
                    print(f"{r[0]:<5} {r[1]:<15} {r[2]:<5} {r[3]:<15} {r[4]}")

                print()

        elif choice == "3":
            emp_id = int(input_number("Employee ID: "))

            if not manager.employee_exists(emp_id):
                print(Fore.RED + "✘ Employee ID not found.\n")
                continue

            name = input_alpha("New Name: ")
            age = int(input_number("New Age: "))
            dept = input_alpha("New Department: ")

            if manager.update_employee(emp_id, name, age, dept):
                print(Fore.GREEN + "✔ Employee updated!")

                updated = manager.get_employee(emp_id)
                print(Fore.CYAN + "Updated Record:")
                print(f"{Fore.YELLOW}ID: {Fore.WHITE}{updated[0]}")
                print(f"{Fore.YELLOW}Name: {Fore.WHITE}{updated[1]}")
                print(f"{Fore.YELLOW}Age: {Fore.WHITE}{updated[2]}")
                print(f"{Fore.YELLOW}Department: {Fore.WHITE}{updated[3]}")
                print(f"{Fore.YELLOW}Stored At: {Fore.WHITE}{updated[4]}\n")
            else:
                print(Fore.RED + "✘ Update failed.")

        elif choice == "4":
            emp_id = int(input_number("Employee ID: "))

            if manager.delete_employee(emp_id):
                print(Fore.GREEN + "✔ Employee deleted!")
            else:
                print(Fore.RED + "✘ Employee ID not found.")

        elif choice == "5":
            clear_screen()
            continue

        elif choice == "6":
            print(Fore.RED + "Exiting...")
            break

        else:
            print(Fore.RED + "Invalid choice.\n")

if __name__ == "__main__":
    main()
