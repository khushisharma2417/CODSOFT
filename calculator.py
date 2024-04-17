def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

print("Select your option: (1, 2, 3, 4)")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divide")

option = int(input("Enter your option: "))
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if option == 1:
    result = add(a, b)
    print("Result:", result)
elif option == 2:
    result = subtraction(a, b)
    print("Result:", result)
elif option == 3:
    result = multiplication(a, b)
    print("Result:", result)
elif option == 4:
    result = divide(a, b)
    print("Result:", result)
else:
    print("Invalid option")