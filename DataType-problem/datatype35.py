# 35. Write a Python program to iterate over dictionaries using for loops


def iterate_over_dictionary(dict1):
    print("Given dictionary is %s " % dict1)
    for key, value in dict1.items():
        print(key, value)


iterate_over_dictionary({'a': 1, 'b': 2, 'c': 3})
