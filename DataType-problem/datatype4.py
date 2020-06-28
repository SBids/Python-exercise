# 4. Write a Python program to get a single string from two strings, separated by
# a space and swap the first two characters of each string

first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

output = second_string[:2] + first_string[2:] + ' ' + first_string[:2] + second_string[2:]
print(output)
