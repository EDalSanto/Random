def format_duration(seconds):
    """
    Converts seconds into nice format
    """
    seconds_in_year = 31536000
    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_minute = 60
    seconds_in_second = 1
    hf = [['year',0], ['day',0], ['hour',0], ['minute',0], ['second',0]]
    if seconds == 0:
        return "now"
    else: # Way to find how many units of each time measure (i.e., years),
        hf[0][1] = seconds / seconds_in_year
        hf[1][1] = (seconds % seconds_in_year) / seconds_in_day
        hf[2][1] = (seconds % seconds_in_day) / seconds_in_hour
        hf[3][1] = (seconds % seconds_in_hour) / seconds_in_minute
        hf[4][1] = (seconds % seconds_in_minute) / seconds_in_second
    list = [] # Stores time measures in correct format to be joined
    for elm in hf: # Deals with plurality
        if elm[1] == 1:
            list.append(str(1) + " " + elm[0])
        elif elm[1] > 1:
            list.append(str(elm[1]) + " " + elm[0] + "s")
    if len(list) == 1: # No need for for 'and' if list length == 1
        return list[0]
    else: # If list length greater than 1, need to add 'and' before last elm
        last_elm = list.pop(len(list)-1) # Last elm popped off and stored
        ans = ", ".join(list)
        return ans + " and " + last_elm # Then added back at the end

print format_duration(4662)
# 1 hour, 17 minutes and 42 seconds
