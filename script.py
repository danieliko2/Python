import functools
def double_letter(my_str):
    return functools.reduce((lambda x,y: x if x==y else my_str[2]), my_str.join(my_str)[0], my_str.join(my_str)[1])

# print(double_letter("Test"))
print("abc".join("abc"))