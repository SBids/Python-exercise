# 41. Write a Python program to convert a tuple to string


def tuple_to_string(my_tuple):
    print("Given tuple is {0}" .format(my_tuple))
    my_string = ''.join(my_tuple)
    return my_string


print(tuple_to_string(('John', 'writer', '23')))
