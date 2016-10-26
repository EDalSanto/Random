def OffLineMinimum(strArr):
    nums = []
    res = []
    for elm in strArr:
        if elm != 'E':
            nums.append(elm)
        else:
            smallest = min(nums)
            nums.remove(smallest)
            res.append(smallest)
    return ",".join(res)
    
