# 42. Write a program to convert list to a tuple


def list_to_tuple(my_list):
    print("list = {0} ".format(my_list))
    return (*my_list,)


print("Corresponding tuple = {0}".format(list_to_tuple(['John', 'writer', '23'])))
