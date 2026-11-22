class Employee:
    def __init__ (self, employee_id:int, name:str, department:str, salary:float):
        self._employee_id   = employee_id
        self._name          = name
        self._department    = department
        self._salary        = salary

    @property
    def salary(self)-> float:
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if(value < 0):
            raise ValueError("Salary cannot be negative")
        self._salary=value    
        
    
    def increase_salary(self, percentage:float)->None:
        if(percentage <= 0 ):
            raise ValueError("Percentage must be greater than zero")
        #TODO
        #get percentage
        #add to the salary
        salary_percentage = self._salary * (percentage/100)
        self._salary += salary_percentage

    def display_employee_detail(self)->str:
        return (
            f"Employee ID: {self._employee_id}\n"
            f"Name: {self._name}\n"
            f"Department: {self._department}\n"
            f"Salary: {self._salary:.2f}"
        )
        
class Manager(Employee):
    def __init__(self, employee_id, name, department, salary, team_size:int):
        super().__init__(employee_id, name, department, salary)
        if team_size < 0:
            raise ValueError("Team size cannot be negative")
        self._team_size = team_size
    
    # Method overriding
    def display_employee_detail(self) -> str:
        employee_details = super().display_employee_detail()

        return (
            f"{employee_details}\n"
            f"Team Size: {self._team_size}"
        )

class Developer(Employee):
    def __init__(self, employee_id, name, department, salary, programming_language:str):
        super().__init__(employee_id, name, department, salary)
        self._programming_language = programming_language
        

    def display_employee_detail(self):
        employee_details = super().display_employee_detail()
        
        return (
            f"{employee_details}\n"
            f"Programming Language: {self._programming_language}"
        )

employee = Employee(1, "Bilal", "Backend", 2500)

employee.salary = 3000
print(employee.salary)  # 3000

employee.salary = -500  # Raises ValueError
