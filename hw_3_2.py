def get_value():
    try:
        value = int(input("Please enter the number: "))
        return value
    except ValueError:
        print("It's not an integer!!!")
        quit()


def get_operator():
    operator_input = input("Please select the operation:\n1 +\n2 -\n3 *\n4 /\n")
    if operator_input != '1' and operator_input != '2' and operator_input != '3' and operator_input != '4':
        print("Invalid Operator. Please use 1-4 operator")
        quit()
    else:
        return operator_input


def calc(num_1, num_2, operator_input):
    if operator_input == '1':
        result = num_1 + num_2
        print(f"{num_1} + {num_2} = {result}")
    elif operator_input == '2':
        result = num_1 - num_2
        print(f"{num_1} - {num_2} = {result}")
    elif operator_input == '3':
        result = num_1 * num_2
        print(f"{num_1} * {num_2} = {result}")
    elif operator_input == '4':
        try:
            result = num_1 / num_2
            print(f"{num_1} / {num_2} = {result}")
        except ZeroDivisionError:
            print("Impossible to divide by zero!!!")
    return result

calc_status = True
while calc_status:
    value_1 = get_value()
    operator = get_operator()
    value_2 = get_value()
    result = calc(value_1, value_2, operator)
    print(result)

    calc_close = input("Do you still need a calculator:\n1)'y' - Yes\n2)any other - No\n")
    calc_status = True if calc_close == 'y' else False
