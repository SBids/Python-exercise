# 8. Write a Python program to remove the nth index character from a nonempty string.

non_empty_string = input("Enter non empty string: ")
n = int(input("Enter the nth index: "))
output = non_empty_string[:n] + non_empty_string[n+1:]
print("The non empty string is %s " % non_empty_string)
print("The string without {0} index character is {1} ".format(n, output))
