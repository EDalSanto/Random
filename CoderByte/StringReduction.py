def convert_two_to_one(s):
    """
    Returns reduced string
    """
    strings = ['a','b','c']
    for char in s:
        strings.remove(char)
    return strings[0]

def StringReduction(str):
    s = list(str)
    i = 0
    while all([ s[0] == char for char in s]) == False:
        if i >= len(s)-1:
            i = 0
        if s[i] != s[i+1]:
            temp = convert_two_to_one(s[i:i+2])
            s[i:i+2] = temp
        i += 1
    return len(s)

print StringReduction("abcabc")
print StringReduction("aabc") == 1
print StringReduction('abb') == 1
