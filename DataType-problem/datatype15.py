# 15. Write a Python function to insert a string in the middle of a string.


def mid_insertion(string1, string2):
    index = int(len(string1)/2)
    output = string1[:index] + string2 + string1[index:]
    return output


print(mid_insertion('{{}}', 'PHP'))
