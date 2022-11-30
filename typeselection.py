
from fractions import Fraction
import cmath

def IdentifyType(data):
    data_type, first_number, operation, second_number = data

    if data_type == '1':

        first_number = complex(first_number)

        second_number = complex(second_number)

    elif data_type == '2':

        a = first_number
        first_number = Fraction(int(a[0: a.index('/')]),
             int(a[a.index('/')+1:len(a)]))

        b = second_number
        second_number = Fraction(int(b[0: b.index('/')]),
             int(b[b.index('/')+1:len(b)]))

    return (first_number, operation, second_number)