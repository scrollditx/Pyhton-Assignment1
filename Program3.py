# WAP to create a user define function and perform separate arithmetic Operator.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def arithmetic_Operator(a,b): #Defining Function
    # Addition
    addition = a + b
    print(f"Addition:{a} + {b} = {addition}")
    # Subtraction
    subtraction = a - b
    print(f"Subtraction:{a} - {b} = {subtraction}")
    # Multiplication
    multiplication = a * b
    print(f"Multiplication:{a} * {b} = {multiplication}")
    # Division
    division = a / b
    print(f"Division:{a} / {b} = {division}")

arithmetic_Operator(a,b) #Calling Function