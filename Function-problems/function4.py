# 4. Write a Python program to reverse a string


def get_reverse(my_string):
    print("Given string : %s " % my_string)

    # reversed_string = "".join(reversed(my_string))

    reversed_string = my_string[::-1]
    return reversed_string


print("The reversed string : %s" % get_reverse('1234abcd'))
