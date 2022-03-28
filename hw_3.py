import sys

try:
    value_1 = input("Please enter the first number: ")
    value_1 = int(value_1)
except ValueError:
    print("It's not an integer!!!")
    sys.exit()

operator = input("Please select the operation:\n1 +\n2 -\n3 *\n4 /\n")
if operator != '1' and operator != '2' and operator != '3' and operator != '4':
    print("Invalid Operator. Please use 1-4 operator")
    sys.exit()

try:
    value_2 = input("Please enter the second number: ")
    value_2 = int(value_2)
except ValueError:
    print("It's not an integer!!!")
    sys.exit()

if operator == '1':
    result = value_1 + value_2
    print(f"{value_1} + {value_2} = {result}")

elif operator == '2':
    result = value_1 - value_2
    print(f"{value_1} - {value_2} = {result}")

elif operator == '3':
    result = value_1 * value_2
    print(f"{value_1} * {value_2} = {result}")

elif operator == '4':
    try:
        result = value_1 / value_2
        print(f"{value_1} / {value_2} = {result}")
    except ZeroDivisionError:
        print("Impossible to divide by zero!!!")
