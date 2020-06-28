# 6. Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.


def convert_poor(my_string):
    not_string = my_string.find('not')
    poor_string = my_string.find('poor')

    if (poor_string > not_string and poor_string > 0 and not_string > 0):
        my_string = my_string.replace(my_string[not_string:(poor_string + 4)], 'good')
    return my_string


print(convert_poor('This is not that poor'))
