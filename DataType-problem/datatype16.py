# 16. Write a Python program to sum all the items in a list.


def list_sum(item_list):
    items_sum = 0
    for item in item_list:
        items_sum += item
    return items_sum


print(list_sum([1, 2, 88]))

# 2nd approach
# def list_sum2(item_list):
#     return sum(item_list)
#
# print(list_sum2([1, 2, 88]))

