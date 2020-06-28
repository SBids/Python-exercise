# 2. Write a Python function to sum all the numbers in a list


def get_sum(my_list):
    total_sum = 0
    print("Given list : %s " % my_list)
    for item in my_list:
        total_sum += item
    return total_sum

    # return sum(my_list)


print("sum of all the numbers in the list : %s" % get_sum([1, 2, 3, 4, 5, 6]))
