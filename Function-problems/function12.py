# 12. Write a Python program to create a function that takes one argument,
# and that argument will be multiplied with an unknown given number.


def multiply_unknown(num1):
    print("The argument : %s" % num1)
    return lambda x: x * num1


output = multiply_unknown(5)
print("The product of argument and unknown number (44) : %s" % output(44))
