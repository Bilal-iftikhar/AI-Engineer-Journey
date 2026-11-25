from fastapi import FastAPI

from database import Base, engine
from routers.employees import router as employee_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Management API",
    description="FastAPI with PostgreSQL and SQLAlchemy",
    version="2.0.0"
)

app.include_router(employee_router)


@app.get("/")
def home():
    return {"message": "Employee Management API is running"}