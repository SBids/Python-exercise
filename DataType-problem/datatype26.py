# 26. Write a Python program to insert given string at the beginning of all item in the list


def insert_before_word(user_list, given_str):
    given_str += '% s'
    user_list = [given_str % i for i in user_list]
    return user_list


print(insert_before_word([1, 2, 3, 4], 'emp'))