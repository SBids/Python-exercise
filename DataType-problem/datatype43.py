# 43. WAP to remove an item from a tuple


def remove_tuple_item(my_tuple, item):
    print("Given tuple = {0}".format(my_tuple))
    print("Item to be removed = %s" % item)
    list_from_tuple = list(my_tuple)
    list_from_tuple.remove(item)
    output = tuple(list_from_tuple)
    return output


print(remove_tuple_item(('john', 'Rodriquez', 'San Francisco', 'left', 'Outstanding', 28), 'left'))

