# 7. Write a Python function that takes a list of words and returns the length of the
# longest one.


def get_max_length(word_list):
    max_length = -1
    print("Given list of words is %s" % word_list)
    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)

    return max_length


print("The length of longest word is %s " % get_max_length(['This', 'is', 'hard']))
