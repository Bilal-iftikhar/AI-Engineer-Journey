from pydantic import BaseModel, EmailStr, ConfigDict


class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    department_id: int
    salary: float | None = None

class DepartmentResponse(BaseModel):
    id: int
    department_name:str

    model_config = ConfigDict(from_attributes=True)
    

class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    department:DepartmentResponse
    salary: float | None = None

    model_config = ConfigDict(from_attributes=True)

