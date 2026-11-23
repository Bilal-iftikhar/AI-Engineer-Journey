
from fastapi import FastAPI
from routers.employees import router as employee_router

app = FastAPI(
    title="Employee Management API",
    description="Employee Management REST API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Management API"
    }


app.include_router(employee_router)
