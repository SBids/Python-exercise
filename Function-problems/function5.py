# 5. Write a Python function to calculate the factorial(non-negative number)


def get_factorial(my_num):
    if my_num < 0:
        return "Number should be non-negative"
    elif my_num == 0 or my_num == 1:
        return 1
    else:
        return my_num * get_factorial(my_num - 1)


print(get_factorial(4))


