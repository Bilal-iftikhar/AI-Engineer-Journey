from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    department_name = Column(String(100), nullable=False)

    employees = relationship(
        "Employee",
        back_populates="department"
    )


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=False
    )
    salary = Column(Numeric(10, 2), nullable=True)
    #define relationship
    department = relationship(
        "Department",
        back_populates="employees"
    )