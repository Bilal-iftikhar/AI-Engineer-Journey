from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from sqlalchemy.exc import IntegrityError

from database import get_db
from models import Employee 
from schemas import EmployeeCreate, EmployeeResponse

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.get("/", response_model=list[EmployeeResponse])
def get_all_employees(db: Session = Depends(get_db)):
    employees = (
        db.query(Employee)
        .options(joinedload(Employee.department))
        .all()
    )

    return employees

@router.get("/search")
def get_paginated_employees(
    page: int = Query(1, ge=1),
    limit:int = Query(10, ge=1, le=100),
    department_id: int | None = Query(None, ge=1),
    sort_by: str = Query("id"),
    order: str = Query("asc"),
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit
    query = db.query(Employee)
    if department_id is not None:
        query = query.filter(
            Employee.department_id == department_id
        )

    sort_columns = {
        "id": Employee.id,
        "name": Employee.name,
        "salary": Employee.salary
    }
    if sort_by not in sort_columns:
        raise HTTPException(
         status_code=400,
            detail="Invalid sorting field"
        )

    if order.lower() not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Order must be asc or desc"
        )
    sort_column = sort_columns[sort_by]
    sort_method = getattr(sort_column, order.lower())
    query = query.order_by(sort_method())

    # 3. Total matching records (before pagination)
    total = query.count()

    # 4. Pagination
    offset = (page - 1) * limit

    employees = (
        query
        .offset(offset)
        .limit(limit)
        .all()
    )
    return {
        "page": page,
        "limit": limit,
        "total": total,
        "employees": employees
    }
    
@router.get("/paginated")
def get_paginated_employees(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit

    employees = (
        db.query(Employee)
        .filter(Employee.department_id == 1)
        .order_by(Employee.id.asc())
        .offset(offset)
        .limit(limit)
        .all()
    )

    total = db.query(Employee).count()

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "employees": employees
    }

@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee
    

@router.post("/", response_model=EmployeeResponse, status_code=201)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    new_employee = Employee(**employee.model_dump())
    try:
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
        return new_employee
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Email already exists or department is invalid"
        )

@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    employee_data: EmployeeCreate,
    db: Session = Depends(get_db)
):
    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    try:
        for key, value in employee_data.model_dump().items():
            setattr(employee, key, value)

        db.commit()
        db.refresh(employee)

        return employee

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Email already exists or department is invalid"
        )

@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()
    
    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db.delete(employee)
    db.commit()

    return {
        "message": "Employee deleted successfully",
        "employee_id": employee_id
    }
    