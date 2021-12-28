import functools

def four_dividers(number):
    return filter((lambda x: x % 4 == 0), range(number+1))

print(list(four_dividers(16)))