import cmath

def CalcModule(data):
    first_number, operation, second_number = data
    if operation == '+':
        return sum(first_number, second_number)
    if operation == '-':
        return sub(first_number, second_number)
    if operation == '*':
        return mult(first_number, second_number)
    if (operation =='/') and (second_number != 0):
        return div(first_number, second_number)
    if (operation =='/') and (second_number != 0):
        return 'Ошибка : /0'

def sum(first_number, second_number):
    return first_number + second_number

def sub(first_number, second_number):
    return first_number - second_number

def mult(first_number, second_number):
    return first_number * second_number

def div(first_number, second_number):
    return first_number / second_number