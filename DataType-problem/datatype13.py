# 13. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).

word_list = input("Input comma separated sequence of words : ")
words = [word.strip() for word in word_list.split(",")]
print(",".join(sorted(list(set(words)))))
