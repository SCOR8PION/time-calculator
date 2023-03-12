def add_time(start, duration, day=None):

    start_colon_index = start.find(":")
    time_colon_index = duration.find(":")
    last_minute = 0
    last_hour = 0
    day_of_week = 0
    extra_hour = 0
    count = 0
    afternoon_count = 0
    afternoon = ''
    ampm = ''
    

    if(start_colon_index==1):
        start_hour = int(start[0])
        start_minute = str(start[2] + start[3])
        start_minute = int(start_minute)
        ampm = str(start[5] + start[6])
        
    if(start_colon_index==2):
        start_hour = str(start[0] + start[1])
        start_hour = int(start_hour)
        start_minute = str(start[3] + start[4])
        start_minute = int(start_minute)
        ampm = str(start[6] + start[7])

    if(time_colon_index==1):
        time_hour = int(duration[0])
        time_minute = str(duration[2] + duration[3])
        time_minute = int(time_minute)
        
    if(time_colon_index==2):
        time_hour = str(duration[0] + duration[1])
        time_hour = int(time_hour)
        time_minute = str(duration[3] + duration[4])
        time_minute = int(time_minute)
    
    if(time_colon_index==3):
        time_hour = str(duration[0] + duration[1] + duration[2])
        time_hour = int(time_hour)
        time_minute = str(duration[4] + duration[5])
        time_minute = int(time_minute)        

    if(time_minute+start_minute<60):
        last_minute = (time_minute+start_minute)
        if(last_minute<10):
            last_minute= "0" + str(last_minute)
            
    else:
        extra_hour+=1
        last_minute = ((time_minute+start_minute) - 60)
        if(last_minute<10):
            last_minute= "0" + str(last_minute)
    
    if(time_hour+start_hour<12):
        last_hour = time_hour+start_hour
    else:
        hours = time_hour+start_hour
        last_hour = hours % 12
        while(hours >= count):
            count = count+24
            day_of_week+=1
    if(extra_hour==1):
        last_hour+=1
    
    quick = (time_hour + start_hour + extra_hour)

    if(ampm == 'AM'):
        if(quick<12):
            afternoon='AM'
        else:    
            for i in range(1, quick+1):
              if(i % 12 == 0):
                afternoon_count+=1
            if(afternoon_count==1):
                afternoon='PM'
            elif(afternoon_count%2==0):
                afternoon='AM'    
            else:
                afternoon='PM'

    if(ampm == 'PM'):
        if(quick<12):
            afternoon='PM'
        else:    
            for i in range(1, quick+1):
                if(i % 12 == 0):
                    afternoon_count+=1
            if(afternoon_count==1):
                afternoon='AM'
            elif(afternoon_count%2==0):
                afternoon='PM'    
            else:
                afternoon='AM'
    
    list_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if(ampm=='AM'):
       day_of_week = day_of_week-1
    if(day):
        lower_day = day.lower()
        if(lower_day=='monday'):
            for i in range(0, 7):
                if(day_of_week%7 == i):
                    lower_day=list_of_days[i]
        if(lower_day=='tuesday'):
            list_of_days.remove("Monday")
            list_of_days.append("Monday")
            for i in range(0, 7):
                if(day_of_week%7==i):
                    lower_day=list_of_days[i]
        if(lower_day=='wednesday'):
            list_of_days.remove("Monday")
            list_of_days.remove("Tuesday")
            list_of_days.extend(["Monday", "Tuesday"])
            for i in range(0, 7):
                if(day_of_week%7 == i):
                    lower_day=list_of_days[i]
        if(lower_day=='thursday'):
            if(day_of_week%7==5):
                lower_day="Tuesday"
            if(day_of_week%7==6):
                lower_day="Wednesday"
            if(day_of_week%7==0):
                lower_day="Thursday"
            if(day_of_week%7==1):
                lower_day="Friday"
            if(day_of_week%7==2):
                lower_day="Saturday"
            if(day_of_week%7==3):
                lower_day="Sunday"
            if(day_of_week%7==4):
                lower_day="Monday"
        if(lower_day=='friday'):
            if(day_of_week%7==4):
                lower_day="Tuesday"
            if(day_of_week%7==5):
                lower_day="Wednesday"
            if(day_of_week%7==6):
                lower_day="Thursday"
            if(day_of_week%7==0):
                lower_day="Friday"
            if(day_of_week%7==1):
                lower_day="Saturday"
            if(day_of_week%7==2):
                lower_day="Sunday"
            if(day_of_week%7==3):
                lower_day="Monday"
        if(lower_day=='saturday'):
            if(day_of_week%7==3):
                lower_day="Tuesday"
            if(day_of_week%7==4):
                lower_day="Wednesday"
            if(day_of_week%7==5):
                lower_day="Thursday"
            if(day_of_week%7==6):
                lower_day="Friday"
            if(day_of_week%7==0):
                lower_day="Saturday"
            if(day_of_week%7==1):
                lower_day="Sunday"
            if(day_of_week%7==2):
                lower_day="Monday"
        if(lower_day=='sunday'):
            if(day_of_week%7==2):
                lower_day="Tuesday"
            if(day_of_week%7==3):
                lower_day="Wednesday"
            if(day_of_week%7==4):
                lower_day="Thursday"
            if(day_of_week%7==5):
                lower_day="Friday"
            if(day_of_week%7==6):
                lower_day="Saturday"
            if(day_of_week%7==0):
                lower_day="Sunday"
            if(day_of_week%7==1):
                lower_day="Monday"
        

    
    new_time = str(last_hour)
    new_time+=str(":")
    new_time+=(str(last_minute) + ' ' + afternoon)
    if(day):
        new_time+= ', '+lower_day
    if(day_of_week == 1):
        new_time += ' (next day)'
    if(day_of_week > 1):
        new_time+=' (' + str(day_of_week) + ' days later)'



    return new_time