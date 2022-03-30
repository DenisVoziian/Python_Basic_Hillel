calc_status = True
while calc_status:
    try:
        value_1 = int(input("Please enter the first number: "))
        operator = input("Please select the operation:\n1 +\n2 -\n3 *\n4 /\n")
        if operator not in ('1', '2', '3', '4'):
            print("Invalid Operator. Please use 1-4 operator")
            break
        value_2 = int(input("Please enter the second number: "))
        if operator == '1':
            result = value_1 + value_2
            sign = '+'
        elif operator == '2':
            result = value_1 - value_2
            sign = '-'
        elif operator == '3':
            result = value_1 * value_2
            sign = '*'
        elif operator == '4':
            result = value_1 / value_2
            sign = '/'
        print(f'{value_1} {sign} {value_2} = {result}')
    except ValueError:
        print("It's not an integer!!!")
    except ZeroDivisionError:
        print("Impossible to divide by zero!!!")
    finally:
        close_calc = input("Do you still need a calculator:\n1)'y' - Yes\n2)any other - No\n")
        calc_status = True if close_calc == 'y' else False
