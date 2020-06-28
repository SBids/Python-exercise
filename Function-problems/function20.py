# 20. Write a Python program to find intersection of two given arrays using Lambda.


def get_intersection(array1, array2):
    print("The two array are {0} and {1}".format(array1, array2))
    output = list(filter(lambda x: x in array1, array2))
    return output


print("The intersection of two given array is %s" % get_intersection([2, 3, 5, 7, 11], [3, 5, 7, 9, 11]))
