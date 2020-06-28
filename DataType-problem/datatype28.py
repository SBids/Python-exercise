# 28. Write a Python script to add a key to a dictionary


def add_dictionary(previous_dict, added_dict):
    print("The given dictionary is %s" % previous_dict)
    print("The key value pair to be added to given dictionary is %s" % added_dict)
    previous_dict.update(added_dict)
    return previous_dict


print(add_dictionary({0: 10, 1: 20}, {2: 30}))
