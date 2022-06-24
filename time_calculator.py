def add_time(start, duration,day=""):

    #-- hours and minutes 

    hours, minutes = start.split(":")
    format = minutes.split(" ")[1]
    minutes = minutes.split(" ")[0]

    durationHours, durationMinutes = duration.split(":")

    day = 0

    #-- 24-hours clock format

    if format == "PM" :
        hours = int(hours) + 12
        hours = str(hours)

    #-- add hours and minutes
    H = int(hours) + int(durationHours)
    M = int(minutes) + int(durationMinutes)

    #-- Hours and minutes conversion 
    while M >= 60 : 
        H +=1
        M -= 60

    if H >= 24 :
        day += H//24

    while H >= 24 :
        H -= 24


    #-- AM and PM conversion -> 12-hour clock format 
    if H > 0 and H < 12 :
        format = "AM"
    elif H == 12 :
        format = "PM"
    elif H > 12 :
        format = "PM"
        H -= 12 #-- Reconversion to 12-hour clock format 
    else :
        format = "AM"
        H += 12
    

    return format ,hours, minutes, durationHours, durationMinutes,H,M, day
#    return new_time
print(add_time("6:30 PM", "205:12"))