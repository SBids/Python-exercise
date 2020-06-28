# 17. Write a Python program to multiplies all the items in a list.


def list_multiplication(item_list):
    total_product = 1
    for item in item_list:
        total_product *= item
    return total_product


print(list_multiplication([5, 5, -1, 2]))
