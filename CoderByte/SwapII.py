def swap_case(str):
    new_str = ""
    for char in str:
        if char.isupper():
            new_str += char.lower()
        else:
            new_str += char.upper()
    return new_str

def SwapII(str):
    s = list(str)
    num_count = 0
    last_num_index = None
    for index,char in enumerate(s):
        if char.isalpha():
            s[index] = swap_case(char)
        elif char.isdigit():
            num_count += 1
            if num_count == 2:
                if s[index-1].isalpha(): # Need to make sure we don't just have two consecutive numbers
                    s[last_num_index],s[index] = s[index],s[last_num_index]
                num_count = 0
            last_num_index = index
        else: # Char is not a letter or digit
            num_count = 0 # just need to reset number count
    return "".join(s)

print SwapII("Hello -5LOL6") == 'hELLO -6lol5'
print SwapII( "6Hello4 -8World, 7 yes3") == '4hELLO6 -8wORLD, 7 YES3'
print SwapII("12345g4g))((") == '12344G5G))(('
