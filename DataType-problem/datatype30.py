# 30. Write a Python script to check whether a given key already exists in a dictionary.


def check_key(my_dict, key):
    print("The given dictionary is %s" % my_dict)
    print("The key : %s " % key)
    if key in my_dict.keys():
        return "exist"
    else:
        return "not  exist"


print(check_key({'name': 'Ram', 'surname': 'Lohani', 'address': 'Kapilvastu'}, 'name'))