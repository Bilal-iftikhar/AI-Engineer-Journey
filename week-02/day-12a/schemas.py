from pydantic import BaseModel, EmailStr, ConfigDict


class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    department_id: int
    salary: float | None = None


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    department_id: int
    salary: float | None = None

    model_config = ConfigDict(from_attributes=True)