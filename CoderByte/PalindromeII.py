def PalindromeTwo(str):
    clean_str = ""
    for char in str:
        if char.isalpha():
            clean_str += char.lower()
    if clean_str == clean_str[::-1]:
        return 'true'
    return 'false'

print PalindromeTwo("not- ? a palindrome") == 'false'
