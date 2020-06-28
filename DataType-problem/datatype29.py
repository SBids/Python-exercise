# 29. Write a python script to concatenate following dictionaries to create new one


def concatenate_dictionary(dic1, dic2, dic3):
    dic4 = {}
    print("Given dictionaries are {0}, {1}, {2}".format(dic1, dic2, dic3))
    for dic in (dic1, dic2, dic3):
        dic4.update(dic)
    return dic4


print(concatenate_dictionary({1: 20, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}))
