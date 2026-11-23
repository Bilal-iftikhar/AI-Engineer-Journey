from database import get_connection
from employee_repository import (
    delete_employee,
    get_employee_by_id,
    create_employee,
    update_employee
)


def test_connection():
    try:
        with get_connection() as connection:
            print("Connected successfully!")
    except Exception as error:
        print("Database connection failed:", error)


if __name__ == "__main__":
    # Get all employees
    # employees = get_all_employees()
    # print("All Employees:", employees)
    
    # deleted = delete_employee(10)

    # if deleted is None:
    #     print("Employee not found!")
    # else:
    #     print("Deleted employee:", deleted)

    # # Get employee by ID
    # employee = get_employee_by_id(10)
    # if employee is None:
    #     print("Employee not found!")
    # else:
    #     print("Employee:", employee)

    # Create employee
    # new_employee = create_employee(
    #     "Bilal",
    #     "bilalq@example.com",
    #     20
    # )
    # print("Created:", new_employee)

    # Update employee salary
    employee = create_employee(
                "Afnan", "afnan@gmail.com", 2
                )
    print("Updated:",employee)