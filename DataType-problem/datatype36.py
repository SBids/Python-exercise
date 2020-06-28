# 36. Write a Python program to sum all the items in a dictionary


def get_sum(dict1):
    item_sum = 0
    for i in dict1:
        item_sum += dict1[i]

    return item_sum


print(get_sum({'a': 1, 'b': 2, 'c': 3}))

# 2nd approach
# def get_sum1(dict1):
#     return (sum(dict1.values()))
# print(get_sum1({'a': 1, 'b': 2, 'c': 3}))
