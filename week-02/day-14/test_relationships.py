from database import SessionLocal
from models import Employee, Department

db = SessionLocal()

try:
    # Get an employee
    employee = db.query(Employee).first()

    if employee:
        print("Employee:", employee.name)
        print("Department:", employee.department.department_name)

    # Get a department
    department = db.query(Department).first()

    if department:
        print("\nDepartment:", department.department_name)

        for employee in department.employees:
            print("Employee:", employee.name)

finally:
    db.close()