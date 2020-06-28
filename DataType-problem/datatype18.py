# 18. Write a Python program to get the largest number from a list.


def get_largest_number(num_list):
    print("Given list of number : %s" % num_list)
    largest_number = sorted(num_list)
    return largest_number[-1]


print("The largest number in the given list : %s" % get_largest_number([12, 34, 55]))


# 2nd approach
# def get_largest_number2(num_list):
#     return max(num_list)
#
#
# print(get_largest_number2([12, 34, 55]))
