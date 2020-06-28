# 44. Write a Python program to slice a tuple


def tuple_slicing(my_tuple, start=0, end=-1, step=1):
    print("Given tuple = {0}" .format(my_tuple))
    sliced_tuple = my_tuple[start:end:step]
    return sliced_tuple


print(tuple_slicing((1, 2, 3, 4, 5, 6, 7, 8, 9), 2, 8))
