from database import get_connection

employee_list = [
    {"id": 1, "name": "Ali", "department": "IT"},
    {"id": 2, "name": "Ahmed", "department": "HR"}
]


def get_all_employees(department: str | None = None):
    with get_connection() as connection:
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM employees")

            employees = cursor.fetchall()

            for employee in employees:
                print(employee)



def get_employee_by_id(employee_id: int):
    return next(
        (emp for emp in employee_list if emp["id"] == employee_id),
        None
    )


def create_employee(data: dict):
    if get_employee_by_id(data["id"]):
        return None

    employee_list.append(data)
    return data


def update_employee(employee_id: int, data: dict):
    employee = get_employee_by_id(employee_id)

    if employee is None:
        return None

    employee["name"] = data["name"]
    employee["department"] = data["department"]

    return employee


def delete_employee(employee_id: int):
    employee = get_employee_by_id(employee_id)

    if employee is None:
        return None

    employee_list.remove(employee)
    return employee
def get_employee_count():
    return len(employee_list.copy())
    
