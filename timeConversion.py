def timeConversion(s):
    hours, minutes, seconds = s[:-2].split(":")
    if s.endswith("AM"):
        hours = '00' if hours == '12' else hours
    else:
        hours = str(int(hours) % 12 + 12) if hours != '12' else hours
    return f"{hours.zfill(2)}:{minutes}:{seconds}"



def timeConversion(s):
    hours, minutes, seconds = s[:-2].split(":")
    intHours = int(hours)
    
    if intHours == 12 and s.endswith("AM"):
        intHours = 0
    
    if intHours != 12 and s.endswith("PM"):
        intHours += 12
        
    hour = intHours
    if intHours < 10:
        return f"0{hour}:{minutes}:{seconds}"
    else:
        return f"{hour}:{minutes}:{seconds}" 