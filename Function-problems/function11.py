# 11. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies
# argument x with argument y and print the result.

sum_15 = lambda a: a + 15
print("The sum of argument and 15 is : %s" % sum_15(34))

arg_product = lambda x, y: x * y
print("The product of x and y : %s" % arg_product(2, 99))

