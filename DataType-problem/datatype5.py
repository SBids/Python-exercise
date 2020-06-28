# 5 Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.

sample_string = input("Enter the string: ")
if len(sample_string) > 2:
    output = sample_string+'ing' if(sample_string[-3:] != 'ing') else sample_string+'ly'
else:
    output = sample_string


print(output)
