# 40. Write a Python program to add an item in tuple


def add_item_tuple(my_tuple, item):
    print("Given tuple : {0}".format(my_tuple))
    print("Item to be added to given tuple : %s" % item)
    final_tuple = my_tuple + (item,)
    return final_tuple


print(add_item_tuple(('John', 'writer', 23), 'hello'))
