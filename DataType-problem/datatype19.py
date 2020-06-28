# 19. Write a Python program to get the smallest number from a list.


def get_smallest_number(num_list):
    print("Given list : %s" % num_list)
    smallest_number = sorted(num_list)
    return smallest_number[0]


print("The smallest list in the given list : %s" % get_smallest_number([121, 34, 550, 66, 754]))

# 2nd approach
# def get_smallest_number2(num_list):
#     return min(num_list)
# print("The smallest list in the given list : %s" % get_smallest_number2([121, 34, 550, 66, 754]))



