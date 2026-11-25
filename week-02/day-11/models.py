from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from database import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    department_name = Column(String(100), nullable=False)

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