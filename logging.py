from datetime import datetime as dt
from time import time


def LogEntry(data, result):
    first_number, operation, second_number = data
    recording = f'{str(first_number)} {operation} {str(second_number)}'
    time = dt.now().strftime('%H:%M')
    
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write('{}; операция : {} результат :{}\n'.format(
            time, recording, result))