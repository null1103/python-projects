'''
This project will implement a basic calculator which performs the four basic operations on provided integers:
addition, subtraction, multiplication, division
'''

num1 = float(input("Enter first number: "))
op = (input("Enter operator: "))
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "*":
    print(num1 * num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid Operator")


# Ask user to enter two integers

# Ask user which operation they would like to perform

# Perform the calculation

# Print the result of the calculation
