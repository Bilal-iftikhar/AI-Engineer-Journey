
from pydantic import BaseModel, Field, field_validator


class EmployeeCreate(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=20,
        pattern=r"^[a-zA-Z0-9_]+$"
    )
    department: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value


class EmployeeUpdate(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=20,
        pattern=r"^[a-zA-Z0-9_]+$"
    )
    department: str
