def DashInsertII(num):
    new_int = ""
    s = str(num)
    for i in range(len(s)-1):
        if int(s[i]) % 2 == 0 and int(s[i+1]) % 2 == 0:
            if int(s[i]) == 0 or int(s[i+1]) == 0:
                new_int += s[i]
            else:
                new_int += "%s*" % s[i]
        elif int(s[i]) % 2 != 0 and int(s[i+1]) % 2 != 0:
            new_int += "%s-" % s[i]
        else:
            new_int += s[i]
    new_int += s[-1]
    return new_int

print DashInsertII(99946) == '9-9-94*6'
print DashInsertII(56647304) == '56*6*47-304'
print DashInsertII(10120) == '10120'
print DashInsertII(60497642) == '6049-76*4*2'
