# 11. Write a Python program to count the occurrences of each word in a given
# sentence.
sentence = input("Enter the sentence: ")
word_list = sentence.split()
word_count = {i: word_list.count(i) for i in set(word_list)}
print(word_count)
