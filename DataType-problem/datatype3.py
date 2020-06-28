# 3. Write a Python program to get a string from a given string where all
# occurence of its first char have been changed to '$', except the first char itself


def replace_character(my_string):
    print("Given string : %s" % my_string)
    first_character = my_string[0]
    output = first_character + my_string[1:].replace(first_character, '$')
    return output


print(replace_character('restart'))


