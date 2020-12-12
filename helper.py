import re 
import random
import string

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
    
    if hour > 1:
        if minute > 1:
            duration = str(hour) + " Stunden und " + str(minute) + " Minuten"
        elif minute == 0:
            duration = str(hour) + " Stunden"
        else:
            duration = str(hour) + " Stunden und " + "eine Minute"
    elif hour == 1:
        if minute > 1:
            duration = "eine Stunde und " + str(minute) + " Minuten"
        elif minute == 0:
            duration = "eine Stunde"
        else:
            duration = "eine Stunde und eine Minute"
    else:
        if minute > 1:
            duration = str(minute) + " Minuten"
        else:
            duration = "eine Minute"

    return duration

def get_random_string(length):
    letters = string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return  result_str

if __name__ == '__main__':
    # duration = 'PT1H30M15S'
    # duration = 'PT15M1S'

    # duration = parse_duration(duration)
    
    # print(duration)
    print(get_random_string(4))
