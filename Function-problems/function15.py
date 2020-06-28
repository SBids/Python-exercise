# 15. Write a Python program to filter a list of integers using Lambda.


def filter_integer(list_of_integers):
    print("Given list : %s" % list_of_integers)
    output = list(filter(lambda x: (x % 11 == 0), list_of_integers))
    print("The multiple of 11 filtered from the given list : %s " % output)


filter_integer([23, 33, 43, 66, 76, 86, 99])

