class Calculator:
    def __init__(self):
        pass
    def add(self,a:float, b:float)->float:
        return (a + b)                
        
    def divide(self, a:float, b:float)->float:
        if b == 0:
           raise ZeroDivisionError("Cannot divide by zero")
        return (a / b)
    
    def subtract(self, a: float, b: float) -> float:
        return (a - b)

    def multiply(self, a: float, b: float) -> float:
        return (a * b)

calculator = Calculator();

while True:
    print("\n===== PYTHON CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if(choice == 5):
            print("Thank you for using python calculator!")
            break
        if choice not in [1,2,3,4]:
            print("Enter value from 1 to 5")
            continue
        try:
            a = float(input("Enter a number: "))
            b = float(input("Enter a number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue
        else :
            if(choice == 1):
                addition = calculator.add(a, b)
                print("Addition:", addition)
            elif(choice == 2):
                subtraction = calculator.subtract(a, b)
                print("Subtraction:", subtraction)
            elif(choice == 3):
                multiply = calculator.multiply(a, b)
                print("Multiply:", multiply)
            elif(choice == 4):
                division = calculator.divide(a, b)
                print("Division :", division)
                
    except ValueError:
        print("Value should be integer")
    except ZeroDivisionError as error:
        print("Calculation error:", error)
    finally:
        print("Calculator operation completed.")
    
        