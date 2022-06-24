def add_time(start, duration,firstDay=""):

    #-- hours and minutes 

    hours, minutes = start.split(":")
    format = minutes.split(" ")[1]
    minutes = minutes.split(" ")[0]

    durationHours, durationMinutes = duration.split(":")

    days = 0

    weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", 
                "Friday", "Saturday", "Sunday"]

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
        days += H//24

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

    #-- Number of day passed 
    if days > 0 :
        if days == 1 :
            day = " (next day)"
        elif days > 1 :
            day = " (" + str(days) + " days later)"
    else : 
        day = ""

    #-- Week days
    if firstDay : 
        weeks = days // 7
        i = weekDays.index(firstDay.lower().capitalize()) + (days - 7 * weeks)
        if i > 6 :
            i -= 7
        day_ = ", " + weekDays[i]
    else :
        day_ = ""
      
    #-- Printing format 
    new_time = str(H) +":"+ (str(M) if M > 9 else ("0" + str(M))) + " " + format + day_ + day
    return new_time

