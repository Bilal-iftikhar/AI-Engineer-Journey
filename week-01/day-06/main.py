from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

app = FastAPI(
    title="Employee Management API",
    description="My first REST API using FastAPI",
    version="1.0.0"
)

employee_list = [
        {"id": 1, "name": "Ali", "department": "IT"},
        {"id": 2, "name": "Ahmed", "department": "HR"},
    ]
@app.get("/")
def home():
    return {"message": "Welcome to Employee Management API"}


@app.get("/employees")
def get_employees(department: str | None = None) -> list[dict]:
    if department is None:
        return employee_list

    employees = [
        emp for emp in employee_list
        if emp["department"].lower() == department.lower()
    ]

    return employees

# Get employee by ID
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    employee = next(
        (emp for emp in employee_list if emp["id"] == employee_id),
        None
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail=f"Employee with ID {employee_id} not found"
        )

    return employee


class User(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=20,
        pattern=r"^[a-zA-Z0-9_]+$"
    )
    department: str
    #salary: float = Field(..., gt=0)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value

# Add employee
@app.post("/employees", status_code=201)
def add_employee(data: User):
    existing_employee = next(
        (emp for emp in employee_list if emp["id"] == data.id),
        None
    )

    if existing_employee:
        raise HTTPException(
            status_code=409,
            detail=f"Employee with ID {data.id} already exists"
        )

    new_employee = data.model_dump()
    employee_list.append(new_employee)

    return {
        "message": "Employee created successfully",
        "employee": new_employee
    }

@app.put("/employees/{employee_id}", status_code=200)
def update_employee(employee_id: int, updated_data: User):
    employee = next( (emp for emp in employee_list if emp["id"] == employee_id ), None)
    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    employee["name"] = updated_data.name
    employee["department"] = updated_data.department

    return {
        "message": "Employee updated successfully",
        "employee": employee
    }

@app.delete("/employees/{employee_id}", status_code=200)
def delete_employee(employee_id: int):
    for index, emp in enumerate(employee_list):
        if(emp['id'] == employee_id):
            deleted_employee = employee_list.pop(index)            
            return {
                "message": "Employee deleted successfully",
                "employee": deleted_employee
            }
    # If the loop finishes without finding the ID, return a 404 error
    raise HTTPException(
        status_code=404,
        detail=f"Employee with ID {employee_id} not found"
    )