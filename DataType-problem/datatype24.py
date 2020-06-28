# 24. Write a program to clone or copy list


def get_copy(user_list):
    print("Given list : %s" % user_list)
    output_list = user_list[:]
    return output_list


print("The copy of given list is %s" % get_copy([1, 2, 3]))

# There are other methods too to copy like extend(),list(), shallow copy, deep copy , however
# slicing method is the faster
