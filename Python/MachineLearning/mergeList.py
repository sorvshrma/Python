def merge(list1, list2):
    merged_list = []
    for i in range(0, max((len(list1), len(list2)))):
        if len(list1) < len(list2):
            list1.append('')
            merged = (list1[i], list2[i])
            merged_list.append(merged)
        if len(list1) > len(list2):
            list2.append('')
            merged = (list1[i], list2[i])
            merged_list.append(merged)
        if len(list1) == len(list2):
            merged = (list1[i], list2[i])
            merged_list.append(merged)
    return merged_list


# Driver code
list1 = [1, 2, 3, 6 , 7 , 8]
list2 = ['a', 'b', 'c']
print(merge(list1, list2))