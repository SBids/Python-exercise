# 10. Write a Python program to print the even numbers from a given list


def get_even_number(my_list):
    even_number = []
    print("Given list : %s" % my_list)
    for item in my_list:
        if (item % 2 == 0):
            even_number.append(item)
    print("List with even number only : %s " % even_number)


get_even_number([1, 2, 3, 4, 5, 6, 7, 8, 9])
