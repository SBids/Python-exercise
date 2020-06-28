# 10. Write a Python program to remove the characters which have odd index
# values of a given string.
sample_string = input("Enter the string: ")
output = ''

for i in range(len(sample_string)):
    if i % 2 == 0:
        output = output + sample_string[i]

print(output)
