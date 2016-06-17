def insert_commas(f):
    new_str = ""
    left = f.split(".")[0] # Numbers to left of decimal
    for index,char in enumerate(left):
        if (len(left)-index) % 3 == 0:
            new_str += ",%s" % char
        else:
            new_str += char
    right = f.split(".")[1]
    while len(right) < 4: # In case numbers to right of decimal less than 4
        right += '0'
    new_str += ".%04d" % int(dec)
    return new_str


def FormattedDivision(num1,num2):
    res = round(float(num1)/num2,4)
    return str(insert_commas(str(res)))

print FormattedDivision(9112,2) == 4,556.0000
