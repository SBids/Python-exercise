# 2. Write a Python program to get a string  made of the first 2 and the last 2 chars
# from a given string. If the string length is less than 2, return instead of the empty string

sample_string = input("Enter the string: ")

output = sample_string[:2] + sample_string[-2:] if len(sample_string) >= 2 else ''
print(output)
