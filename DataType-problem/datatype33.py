# 33. Write  a Python script to print a dictionary where the keys are numbers between 1 and 15
# (both included) and the values are  square of keys


def get_dictionary():
    d = {x: x*x for x in range(1, 16)}
    print(d)


get_dictionary()
