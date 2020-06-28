# 16. Write a Python program to square and cube every number in a given list of integers using Lambda.


def square_and_cube(list_of_integers):
    print("Given list of integers : %s" % list_of_integers)
    sq = list(map(lambda x : x*x, list_of_integers))
    cube = list(map(lambda x: x * x * x, list_of_integers))
    print("The list of square of every number in given list : %s" % sq)
    print("The list of cube of every number in given list : %s" % cube)


square_and_cube([2, 5, 7, 9])
