# 3. Write Python function to multiply all the numbers


def get_product(my_list):
    product = 1
    print("Given list : %s " % my_list)
    for item in my_list:
        product *= item
    return product


print("The product of all numbers: %s" % get_product([8, 2, 3, -1, 7]))
