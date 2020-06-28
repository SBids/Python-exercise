# 6. Write a Python function to check whether a number is in range


def check_range(my_num, range_start, range_end):
    if my_num in range(range_start, range_end):
        print("The number is within range")
    else:
        print("The number is not in range")


check_range(1, 5, 10)
