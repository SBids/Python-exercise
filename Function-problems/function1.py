# 1. Write a Python function to find the Max of three numbers


def get_max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3

    # max can be used after convert the numbers to list of number
    # num_list = [num1, num2, num3]
    # return max(num_list)


print(get_max(-30, -2, -30))
