def to_minutes(s):
    """
    Converts string time into minutes
    """
    t = [ int(elm) for elm in s[:-2].split(":") ] # creating hour, minute lists
    if s.endswith('pm') and t[0] != 12:
        t[0] += 12 # Converting pm to 24 hours
    elif s.endswith('am') and t[0] == 12:
    	t[0] -= 12
    return t[0] * 60 + t[1]

print to_minutes('12:40am')
print to_minutes('5:40am')

def CountingMinutesI(str):
    """
    Converts a string of two times into their difference in minutes

    str: two times, i.e.,: '1:23am-1:08am' returns 1425 (almost 24 hours)

    Returns: integers representing minutes passes between two times
    """
    mins = [ to_minutes(t) for t in str.split('-') ]
    res = mins[1] - mins[0]
    if res < 0:
        return 1440 + res
    return res

print CountingMinutesI("1:23am-1:08am") == 1425
print CountingMinutesI('12:40am-5:40am') == 300
