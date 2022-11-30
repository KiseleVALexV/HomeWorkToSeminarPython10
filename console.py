def OutData(data):
   print(f'Результат вычисления :{data}')

def InputData():
    print('Выберите тип чисел :')
    print('работа с комплексными числами,  введите 1')
    print('работа с рациональными числами, введите 2')
    data_type = input('>')
    if data_type == '1':
        print('Введите первое число в виде "a + bj" :')
        first_number = input()
        print('Выберите операцию :')
        operation = input()
        print('Введите второе число в виде "a + bj" :')
        second_number = input()
    elif data_type == '2':
        print('Введите первое число в виде "a/b") :')
        first_number = input()
        print('Выберите операцию :')
        operation = input()
        print('Введите второе число в виде "a/b") :')
        second_number = input()
    return (data_type, first_number, operation, second_number)