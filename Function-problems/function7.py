# 7. Write a Python function that accepts a string and calculate the number of upper case  letters and lower
# case letters


def count_upper_lower_case(my_string):
    upper_count = 0
    lower_count = 0
    for letter in my_string:
        if(letter >= 'a' and letter <= 'z'):
            upper_count += 1
        if (letter >='A' and letter <= 'Z'):
            lower_count += 1
    print("The string is : %s" % my_string)
    print("No. of Upper case characters : %s" % upper_count)
    print("No. of Lower case characters : %s" % lower_count)


count_upper_lower_case('My new world! Thank you !!!')


# can use isupper() and islower() function too

# def count_upper_lower_case1(my_string):
#     upper_count, lower_count = 0, 0
#     for item in my_string:
#         if item.isupper():
#             upper_count += 1
#         elif item.islower():
#             lower_count += 1
#     print("The number of upper case character is : %s" %upper_count)
#     print("The number of lower case character is : %s" % lower_count)
#
#
# count_upper_lower_case1('My new world! Thank you !!!')
