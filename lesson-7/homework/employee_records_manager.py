class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename

    def add_employee(self, employee):
        if self.search_employee(employee.employee_id):
            print("Employee ID must be unique.")
            return
        with open(self.filename, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        try:
            with open(self.filename, "r") as file:
                employees = file.readlines()
                if not employees:
                    print("No employee records found.")
                    return
                print("Employee Records:")
                for emp in employees:
                    print(emp.strip())
        except FileNotFoundError:
            print("No employee records found.")

    def search_employee(self, employee_id):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    emp_id, name, position, salary = line.strip().split(", ")
                    if emp_id == employee_id:
                        return Employee(emp_id, name, position, salary)
        except FileNotFoundError:
            return None
        return None

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        updated = False
        try:
            with open(self.filename, "r") as file:
                employees = file.readlines()
            with open(self.filename, "w") as file:
                for line in employees:
                    emp_id, emp_name, emp_position, emp_salary = line.strip().split(", ")
                    if emp_id == employee_id:
                        updated = True
                        emp_name = name if name else emp_name
                        emp_position = position if position else emp_position
                        emp_salary = salary if salary else emp_salary
                        file.write(f"{emp_id}, {emp_name}, {emp_position}, {emp_salary}\n")
                    else:
                        file.write(line)
            if updated:
                print("Employee updated successfully!")
            else:
                print("Employee ID not found.")
        except FileNotFoundError:
            print("No employee records found.")

    def delete_employee(self, employee_id):
        deleted = False
        try:
            with open(self.filename, "r") as file:
                employees = file.readlines()
            with open(self.filename, "w") as file:
                for line in employees:
                    emp_id, _, _, _ = line.strip().split(", ")
                    if emp_id == employee_id:
                        deleted = True
                    else:
                        file.write(line)
            if deleted:
                print("Employee deleted successfully!")
            else:
                print("Employee ID not found.")
        except FileNotFoundError:
            print("No employee records found.")

    def menu(self):
        while True:
            print("""
Welcome to the Employee Records Manager!
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit
            """)
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                emp_id = input("Enter Employee ID: ").strip()
                name = input("Enter Name: ").strip()
                position = input("Enter Position: ").strip()
                salary = input("Enter Salary: ").strip()
                self.add_employee(Employee(emp_id, name, position, salary))
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                emp_id = input("Enter Employee ID to search: ").strip()
                employee = self.search_employee(emp_id)
                if employee:
                    print("Employee Found:")
                    print(employee)
                else:
                    print("Employee ID not found.")
            elif choice == "4":
                emp_id = input("Enter Employee ID to update: ").strip()
                name = input("Enter new Name (press Enter to skip): ").strip() or None
                position = input("Enter new Position (press Enter to skip): ").strip() or None
                salary = input("Enter new Salary (press Enter to skip): ").strip() or None
                self.update_employee(emp_id, name, position, salary)
            elif choice == "5":
                emp_id = input("Enter Employee ID to delete: ").strip()
                self.delete_employee(emp_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
