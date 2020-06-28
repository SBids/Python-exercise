# 1. Write a Python program to count the number of characters(character frequency_ in a string

sample_string = input("Enter the string: ")

character_count = {i: sample_string.count(i) for i in set(sample_string)}
print(character_count)
