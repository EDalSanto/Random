# Have the function ArrayAdditionI(arr) take the array of numbers stored in arr and return the string true if any combination of numbers in the array can be added up to equal the largest number in the array, otherwise return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all the same elements, and may contain negative numbers.

# Brute force
def ArrayAdditionI(arr):
    arr.sort()
    target = arr[-1]
    arr.remove(target)
    p_set = [[]] # Powerset of all possible combos
    for num in arr:
        for t in p_set[:]:
            temp = t + [num]
            p_set.append(temp)
            if sum(temp) == target:
                return 'true'
    return 'false'

print ArrayAdditionI([1,2,5,7,16]) == 'false'
print ArrayAdditionI([1,2,3,4]) == 'true'
print ArrayAdditionI([14,10,3,2,2]) == 'true'
print ArrayAdditionI([0,1,4,7,49,54]) == 'true'
