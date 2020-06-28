# 14. Write a program to sort a list of dictionaries using Lambda


def sort_dictionary_list(list_of_dictionary):
    print("Given list of dictionary : %s" % list_of_dictionary)
    score_sorting = sorted(list_of_dictionary, key=lambda x: x['score'])
    house_sorting = sorted(list_of_dictionary, key=lambda x: x['house'])
    reverse_sorting = sorted(list_of_dictionary, key=lambda x: x['score'], reverse=True)
    print("The sorting of list of dictionary based on score : %s  " % score_sorting)
    print("The sorting of list of dictionary based on house : %s  " % house_sorting)
    print("The sorting of list of dictionary based on age in decreasing order : %s  " % reverse_sorting)


sort_dictionary_list([{'house': 'red house', 'score': 50}, {'house': 'green house', 'score': 150}, {'house': 'yellow '
                                                                                                             'house',
                                                                                                    'score': 150},
                      {'house': 'blue house', 'score': 30}])
