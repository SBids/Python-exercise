#18. Write a Python program to check whether a given string is number or not using Lambda.

# is_num = lambda x : True if int(x) else False
#
# print(is_num('-5-'))


integer1 = lambda x: x.replace('.', '', 1).isdigit()
positive_int = lambda y: integer1(y[1:]) if y[0] == '-' else integer1(y)
print("Is -16.4 digit? : %s" % positive_int('-16.4'))
print("Is 16-4 digit? : %s" % positive_int('16-4'))
print("Is 16A4 digit? : %s" % positive_int('16A4'))
