import re 

def parse_duration(duration):

    pattern_hour = '.*(?P<hour>\d)H.*'
    
    result_hour = re.match(pattern_hour,duration)

    if result_hour is not None: 
        hour = int(result_hour.group("hour"))
    else:
        hour = 0
    
    pattern_minute2 = '.*(?P<minute>\d\d)M.*'
    result_minute = re.match(pattern_minute2,duration)

    if result_minute is not None: 
        minute = int(result_minute.group("minute"))
    else:
         pattern_minute = '.*(?P<minute>\d)M.*'
         result_minute = re.match(pattern_minute,duration)
         if result_minute is not None: 
            minute = int(result_minute.group("minute"))
         else:
            minute = 0
    
    if hour > 0:
        if minute > 9:
            duration = str(hour) + ":" + str(minute)
        else:
            duration = str(0) + str(minute) + ":" + str(hour) 
    else:
        if minute > 1:
            duration = str(minute) + " Minuten"
        else:
            duration = "eine Minuten"

    return duration

if __name__ == '__main__':
    duration = 'PT1H30M15S'
    duration = 'PT15M1S'

    duration = parse_duration(duration)
    
    print(duration)