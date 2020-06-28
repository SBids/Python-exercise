# 23. Write a Python program to check a list is empty or not


def check_emptiness(user_list):
    print("Given list : %s" % user_list)
    if len(user_list) == 0:
        return True
    else:
        return False


print(check_emptiness([{}, {}]))