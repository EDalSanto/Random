import itertools

def PermutationStepBrute(num):
    t = itertools.permutations(list(str(num)))
    k = [ int("".join(elm)) for elm in t ]
    k.sort()
    for i in k:
        if i > num:
            return i
    return -1


print PermutationStepBrute(143) == 314
print PermutationStepBrute(11121) == 11211
print PermutationStepBrute(41352) == 41523
print PermutationStepBrute(897654321) == 912345678
