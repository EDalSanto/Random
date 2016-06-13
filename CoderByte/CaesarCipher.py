import string

def CaesarCipher(str,num):
    shifted_str = ""
    for char in str:
        if char.isupper():
            index = string.uppercase.index(char)
            shift = (index+num) % 26
            new_char = string.uppercase[shift]
            shifted_str += new_char
        elif char.islower():
            index = string.lowercase.index(char)
            shift = (index+num) % 26
            new_char = string.lowercase[shift]
            shifted_str += new_char
        else:
            shifted_str += char
    return shifted_str

print CaesarCipher('Hello',4) == 'Lipps'
