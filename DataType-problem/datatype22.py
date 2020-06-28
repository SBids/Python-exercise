# 22. Write a Python program to remove duplicates from a list.


def remove_duplicates(item_list):
    output = []
    for item in item_list:
        if item not in output:
            output.append(item)
    return output


print(remove_duplicates(['the', 'man', 'the', 1, 3, 4, 3, 11, 4]))

# 2nd approach
# def remove_duplicate(item_list):
#     return list(set(item_list))
