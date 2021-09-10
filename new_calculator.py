def calculator(number, second_number, operator):
    if operator == "+":
        return number + second_number
    elif operator == "-":
        return number - second_number
    elif operator == "*":
        return number * second_number
    elif operator == "/":
        return number / second_number
    elif operator == "%":
        return number % second_number
    else:
        raise ValueError


number_one = int(input('Enter first number'))
number_two = int(input('Enter the second number'))
operator = input('Enter the operator')
result = calculator(number_one, number_two, operator)
print(result)
