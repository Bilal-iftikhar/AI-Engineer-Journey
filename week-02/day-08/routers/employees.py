
from fastapi import APIRouter, Depends, HTTPException
from dependencies.pagination import Pagination

from schemas.employee import EmployeeCreate, EmployeeUpdate
from services import employee_service

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

def get_employee_or_404(employee_id: int):
    employee = employee_service.get_employee_by_id(employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee

@router.get("/paginated")
def get_paginated_employees(
    pagination: Pagination = Depends(Pagination)
):
    employees = employee_service.get_all_employees()

    start = pagination.skip
    end = start + pagination.limit

    return {
        "total": len(employees),
        "skip": pagination.skip,
        "limit": pagination.limit,
        "employees": employees[start:end]
    }

@router.get("/{employee_id}")
def get_employee(
    employee: dict = Depends(get_employee_or_404)
):
    return employee