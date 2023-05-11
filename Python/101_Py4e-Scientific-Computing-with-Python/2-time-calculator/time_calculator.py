def add_time(start, duration, day=False):

    # Days
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    new_days = 0
    days = ""

    # Start
    start = start.rsplit(" ")
    temp = start[0].rsplit(":")
    start_hour = int(temp[0])
    start_mins = int(temp[1])
    meridiana = start[1]

    new_hour = 0

    # Working with 24h format
    if meridiana == "PM":
        start_hour += 12

    # Duration
    dur = duration.rsplit(":")
    dur_hour = int(dur[0])
    dur_mins = int(dur[1])

    # Summing mins
    new_mins = start_mins + dur_mins
    if new_mins >= 60:
        new_hour += 1 # +1h
        new_mins -= 60

    #Summing hour
    new_hour += start_hour + dur_hour
    if new_hour >= 24:
        new_days = round(new_hour / 24) # Every 24h +1 day
        new_hour = new_hour % 24

        if new_days == 1:
            days = " (next day)"
        
        if new_days > 1:
            days = " (" + str(new_days) + " days later)"

    if new_hour == 0: # 00:XX becomes 12:00 AM (midnight)
        new_hour = 12
        meridiana = "AM"
    elif new_hour >= 12:
        meridiana = "PM"
        if new_hour > 12:
            new_hour -= 12 # Back to 12h format
    else:
        meridiana = "AM"    

    if type(day) == str:
        if new_days == 0:
            days = ", " + day + days

        if new_days > 0:
            day_index = week.index(day.capitalize()) # Formatting
            day_index += new_days
            day_index = day_index % 7 # Index of correct day
            days = ", " + week[day_index] + days
        
    new_time = str(new_hour) + ":" + str(new_mins).zfill(2) + " " + meridiana + days
    
    return new_time