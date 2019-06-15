def readable(duration, word):
    if duration == 1:
        return '%d %s' % (duration, word)
        
    return '%d %ss' % (duration, word)

def format_duration(seconds):
    if seconds == 0:
        return "now"
        
    minute = 60
    hour = minute * 60
    day = hour * 24
    year = 365 * day
    
    all_units = (
    (year, 'year'),
    (day, 'day'),
    (hour, 'hour'), 
    (minute, 'minute'),
    (1, 'second'),
    )

    expression = []
    
    for unit in all_units:
        time, word = unit
        if seconds >= time:
            duration = int(seconds / time)
            expression.append(readable(duration, word))
            seconds -= duration * time
            
    return " and".join(", ".join(expression).rsplit(",", 1))