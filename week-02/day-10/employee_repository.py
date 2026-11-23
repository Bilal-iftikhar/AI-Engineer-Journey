
from database import get_connection
from psycopg import errors
from psycopg import DatabaseError


def get_all_employees()-> list[tuple]:
    with get_connection() as connection:
        with connection.cursor() as cursor:

            cursor.execute("""
                SELECT id, name, email, department_id, salary
                FROM employees
            """)

            employees = cursor.fetchall()

            return employees
def get_employee_by_id(employee_id:int) -> tuple | None:
    with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                                SELECT id, name, email, department_id, salary
                                FROM employees where id=%s
                            """,(employee_id,))
                return cursor.fetchone()

def create_employee(name:str, email:str, department_id:int) -> tuple | None:
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:

                cursor.execute("""
                    INSERT INTO employees
                        (name, email, department_id)
                    VALUES (%s, %s, %s)
                    RETURNING id, name, email, department_id
                """, (name, email, department_id))

                employee = cursor.fetchone()

                return employee
    except errors.UniqueViolation:
        print("Error: Email already exists!")
        return None
    except errors.ForeignKeyViolation:
        print("Error: Department does not exist!")
        return None

        
def update_employee(employee_id, salary):
    with get_connection() as connection:
        with connection.cursor() as cursor:

            cursor.execute("""
                UPDATE employees
                SET salary = %s
                WHERE id = %s
                RETURNING id, name, salary
            """, (salary, employee_id))

            return cursor.fetchone()
        

def delete_employee(employee_id: int) -> tuple | None:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM employees
                WHERE id = %s
                RETURNING id, name, email
            """, (employee_id,))

            return cursor.fetchone()


def transfer_salary(source_id, target_id, amount):
    with get_connection() as connection:
        with connection.cursor() as cursor:

            cursor.execute("""
                UPDATE employees
                SET salary = salary - %s
                WHERE id = %s
            """, (amount, source_id))

            cursor.execute("""
                UPDATE employees
                SET salary = salary + %s
                WHERE id = %s
            """, (amount, target_id))