# 25. Write a Python program to check whether all dictionaries in a list are empty or not.


def check_dictionary_emptiness(list_of_dictionaries):
    print("Given list of dictionaries : %s" % list_of_dictionaries)
    print(all(not item for item in list_of_dictionaries))


check_dictionary_emptiness([{1, 2}, {}])
check_dictionary_emptiness([{}, {}])
