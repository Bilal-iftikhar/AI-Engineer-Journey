
from fastapi import APIRouter, HTTPException

from schemas.employee import EmployeeCreate, EmployeeUpdate
from services import employee_service

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.get("/")
def get_employees(department: str | None = None):
    return employee_service.get_all_employees(department)


@router.post("/", status_code=201)
def add_employee(data: EmployeeCreate):
    employee = employee_service.create_employee(
        data.model_dump()
    )

    if employee is None:
        raise HTTPException(
            status_code=409,
            detail="Employee already exists"
        )

    return {
        "message": "Employee created successfully",
        "employee": employee
    }


@router.put("/{employee_id}")
def update_employee(employee_id: int, data: EmployeeUpdate):
    employee = employee_service.update_employee(
        employee_id,
        data.model_dump()
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee updated successfully",
        "employee": employee
    }


@router.delete("/{employee_id}")
def delete_employee(employee_id: int):
    employee = employee_service.delete_employee(employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully",
        "employee": employee
    }
@router.get("/count")
def count_employee():
    employee_count = employee_service.get_employee_count()    
    return {
            "message": "Employee count",
            "count": employee_count
        }

@router.get("/{employee_id}")
def get_employee(employee_id: int):
    employee = employee_service.get_employee_by_id(employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee
