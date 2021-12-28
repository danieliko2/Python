import functools

def sum_of_digits(number):
    return functools.reduce((lambda x: x[0]+x[1]), list(number))

print(sum_of_digits(21))