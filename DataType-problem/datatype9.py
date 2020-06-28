# 9. Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.

sample_string = input("Enter the string: ")
output = sample_string[-1:] + sample_string[1:-1] + sample_string[:1]
print("The given string : %s" % sample_string)
print("The string with first and last character exchanged : %s" % output)
