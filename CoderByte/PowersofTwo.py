def PowersofTwo(num):
    """
    Using bitwise operator &(AND) determines whether num is a power of two
    """
    return 'true' if num & (num-1) == 0 else 'false'

print PowersofTwo(8) == 'true'
print PowersofTwo(7) == 'false'
