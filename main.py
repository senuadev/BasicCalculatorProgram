#Basic Calculator

#ask for first number
num1 = int(input("Enter first number: "))

#ask for second number
num2 = int(input("Enter second number: "))

#ask for operator
operator = input("Enter operator (+, -, *, /): ")

#check if operator is valid
if operator == "+":
    print(num1, "+", num2, "=", num1 + num2)
elif operator == "-":
    print(num1, "-", num2, "=", num1 - num2)
elif operator == "*":
    print(num1, "*", num2, "=", num1 * num2)
elif operator == "/":
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("Invalid operator")
