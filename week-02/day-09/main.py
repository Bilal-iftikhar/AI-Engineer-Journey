from services import employee_service
from database import get_connection

def test_connection():
    try:
        connection = get_connection()

        print("Database connected successfully!")

        connection.close()

    except Exception as error:
        print("Database connection failed:", error)


if __name__ == "__main__":
    employee_service.get_all_employees()