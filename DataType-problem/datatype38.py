# 38. Write a Python program to remove a key from a dictionary


def remove_key(dict1, key):
    print("Given dictionary is %s" % dict1)
    print("Key to be removed is %s" % key)
    dict1.pop(key)
    return dict1


print('The remaining dictionary = ' + str(remove_key({'a': 11, 'b': 22, 'c': 3}, 'b')))



