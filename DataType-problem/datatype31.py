# 31. Write  Python program to iterate over dictionaries using for loops


def iterate_dictionary(dict1):
    for item in dict1.items():
        print(item)


iterate_dictionary({'a': 1, 'c': 3, 'd': 4, 'b': 2})