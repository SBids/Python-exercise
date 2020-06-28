# 34. Write a Python script to merge two Python dictionaries


def merge_dictionary(dict1, dict2):
    print("The two dictionaries are {0} and {1}".format(dict1, dict2))
    dict1.update(dict2)
    return dict1


print("The merged dictionary of given dictionaries : %s" % merge_dictionary({"a": 2, "b": 4}, {"c": 1, 2: 8}))
