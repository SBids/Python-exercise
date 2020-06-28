# 8. Write a Python function that takes a list and returns a new list with unique elements of the first line


def get_unique_item(my_list):
    unique_list = []
    print("The list is : %s" % my_list)
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


print("The unique list is : %s" % get_unique_item([2, 22, 4, 43, 3, 3, 2, 6]))

# can be using set() function

# def get_unique_item1(my_list):
#     unique_list = list(set(my_list))
#     return unique_list
#
# print("The list is : [2,22,4,43,3,3,2,6]" )
# print(get_unique_item1([2,22,4,43,3,3,2,6]))
