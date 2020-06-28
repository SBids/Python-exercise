# 13. Write a program to sort a list of tuples using Lambda
def sort_list(my_tuple_list):
    print("Given list of tuples : %s" % my_tuple_list)
    my_tuple_list.sort(key=lambda x: x[1])
    return my_tuple_list


print("The sorted list to with respect to second value of tuple is %s" % sort_list([('red house', 50), ('yellow house', 150), ('green house', 150), ('blue house', 30)]))
