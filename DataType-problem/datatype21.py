# 21. Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.


def last(non_empty_tuple):
    return non_empty_tuple[-1]


def get_sorted_list(list_of_tuple):
    print("Given list of non-empty tuples :" + str(list_of_tuple))
    return sorted(list_of_tuple, key=last)


print(get_sorted_list([(3, 5), (2, 5), (4, 4), (2, 3), (2, 1)]))