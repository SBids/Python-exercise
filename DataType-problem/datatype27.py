# 27. Write a Python program to replace last item with another list


def replace_last_item(list1, list2):
    print("The two lists are {0} and {1} ".format(list1, list2))
    list1[-1:] = list2
    return list1


print(replace_last_item([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))
