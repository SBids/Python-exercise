# 45. Write a Python program to find the index of an item of a tuple


def get_index(my_tuple, item, start=0, end=-1):
    print("Given tuple = {0}".format(my_tuple))
    print("item = {0}, starting from {1}th index item to {2}th index item".format(item, start, end))
    index = my_tuple.index(item, start, end)
    return index


print(get_index(('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'), 'l'))
