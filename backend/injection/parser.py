from datetime import datetime
import re
LOG_PATTERN = re.compile(
    r"(?P<timestamp>[\d\-:\s]+)\s"
    r"(?P<level>\w+)\s"
    r"(?P<service>\w+)\s"
    r"(?P<message>.*?)(?:\suser_id=(?P<user_id>\d+))?$"
)

'''def parse_log_line(line):
    #logic for matching the log pattern
    match = LOG_PATTERN.match(line.strip())
    if not match:
        return None
    return {
          "timestamp": match.group("timestamp"),
        "level": match.group("level"),
        "service": match.group("service"),
        "message": match.group("message")
    }    '''

def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    if not match:
        return None

    data = match.groupdict()
    data["timestamp"] = datetime.strptime(
        data["timestamp"], "%Y-%m-%d %H:%M:%S"
    )
    data["raw"] = line.strip()
    return data 

#Groupdict()
#Strip()
#re.compile()
#python regex are used for searching, matching and extract the data pattern from given text.
#re.compile is a method used to create regex patterns
#r-> raw data
# ?->starting of pattern
#(?P<timestamp>[\d\-:\s]+), (?P<level>\w+), (?P<service>\w+), (?P<message>.*?) is used to capture the names of 
# particualr data
# \s is used to remove the white or extra space from the data
'''groupdict() -> convert raw data into structure data (dictionary)
    r'' -> raw Data
    ?P<timestamp> -> named group
    s+ -> for spaces one or more
    ^ -> start of line
    $ -> end of line
    \S -> non space character'''
# strptime-->Converts timestamp 
# string → datetime object