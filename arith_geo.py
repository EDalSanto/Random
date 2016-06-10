# Have the function ArithGeo(arr) take the array of numbers stored in arr and return the string "Arithmetic" if the sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric pattern. If the sequence doesn't follow either pattern return -1. An arithmetic sequence is one where the difference between each of the numbers is consistent, where as in a geometric sequence, each term after the first is multiplied by some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements.

def ArithGeo(arr):
    # Create diffs
    diffs = []
    for idx,num in enumerate(arr[:-1]):
        diff = arr[idx+1] - num
        diffs.append(diff)
    # Arithmetic? Need all diffs to be same val
    if all([x == diffs[0] for x in diffs]):
        return "Arithmetic"
    # Create ratios
    ratios = []
    for idx,num in enumerate(diffs[:-1]):
        ratio = diffs[idx+1] / num
        ratios.append(ratio)
    # Geometric? Need all diffs to have same ratio
    if all([x == ratios[0] for x in ratios]):
        return "Geometric"

    # Neither
    return -1
