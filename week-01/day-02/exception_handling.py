class ExceptionHandling:
    def __init__(self):
        pass
    def raise_exception(self, number3:int)->str:
        if(number3 > 0 ):
            raise InsufficientFundsError("Custom error")
        
    def divide_number(self, number3:int)->str:
        try:
            number1 = 10 #int(input("Enter a number: "))
            number2 = 2

            result = number1 / number2
        except ZeroDivisionError:
            print("Cannot divide by zero")
        except ValueError:
            print("Enter a valid digit")
        else:
            print("Result:", result)
        finally:
            print("Calculation completed")

class InsufficientFundsError(Exception):
    pass

eh =  ExceptionHandling()
try:
    eh.raise_exception(10)
except InsufficientFundsError as error:
    print(error)



