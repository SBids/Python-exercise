# 37. Write a Python program to multiply all the items in dictionary


def get_product(dict1):
    item_product = 1
    for i in dict1:
        item_product *= dict1[i]
    return item_product


print(get_product({'a': 11, 'b': 22, 'c': -3}))
