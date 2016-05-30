def merge(list1,list2):
    merged = []
    while len(list1) != 0 and len(list2) != 0:
        # Take head of lists because we assume each is sorted
        min1 = list1[0]
        min2 = list2[0]
        if min1 < min2: # Compare lowest value(first elm) of each list
            merged.append(min1)
            list1 = list1[1:]
        else:
            merged.append(min2)
            list2 = list2[1:]
    # Add rest of non-empty list to merged
    if len(list1) == 0:
        merged.extend(list2)
    else:
        merged.extend(list1)
    return merged
#
# print merge([1,2],[5,4])

def mergeSort(list):
    if len(list) == 1: # List of length 1 by definition is sorted
        return list
    else:
        return merge(mergeSort(list[:len(list)/2]), mergeSort(list[len(list)/2:]))

print mergeSort([1,4,3,5,232,53,1,4,3,5,400,0])
# [0, 1, 1, 3, 3, 4, 4, 5, 5, 53, 232, 400]
