class Empoloyee:
    def __init__(self, name:str, amount:float):
        self.name = name
        self.amount = amount

    @property
    def name(self)->str:
        return self._name
    @property
    def amount(self)->float:
        return self._amount

    @name.setter
    def name(self, value:str)->None:
        self._name = value
    @amount.setter
    def amount(self, value:float)->None:
        if(value < 0):
            raise InvalidSalaryError("Value should be creater then 0")

        if(value >= 100000):
                    raise InvalidSalaryError("Salary should not be greater then 100000")
        self._amount = value

    def detail(self):
        return(f"Name : {self.name}\n"
               f"Salary : {self.amount}")
    
class InvalidSalaryError(Exception):
    pass

employees = [
    ("Bilal", 50000),
    ("Hammad", -5000),
    ("Ali", 1500000),
    ("Ahmed", 80000)
]

for name, salary in employees:
    try:
        employee = Empoloyee(name, salary)
        print(employee.detail())
    except InvalidSalaryError as error:
        print(f"Exception: {error}")
    finally:
        print("Employee processing completed")
        print("-" * 35)


