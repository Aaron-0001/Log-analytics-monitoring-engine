import re
from datetime import datetime

LOG_PATTERN = re.compile(
    r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>\w+)\s+"
    r"(?P<service>\w+)\s+"
    r"(?P<message>.*)"
)
def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    if not match:
        return None

    data = match.groupdict()

    data["timestamp"] = datetime.strptime(
        data["timestamp"], "%Y-%m-%d %H:%M:%S"
    )

    return data
# def parse_log_line(line):
#     #logic for matching the log pattern
#     match=LOG_PATTERN.match(line)
#     if not match:
#         return None
#     return {
#         "timestamp": match.group("timestamp"),
#         "level": match.group("level"),
#         "service": match.group("service"),
#         "message": match.group("message")
#     }
#Groupdict()
#Strip()
#re.compile():recompile is a method in python which is used to create regex patterns
#python regex: regular expression are used for searching matching and extract the data pattern from the given text
#r->raw data 
#?->starting of pattern code
#P<timestamp>,P<level>,P<service>,P<message>->these are used to capture the names of a  particular data 
#\s->remove white spaces betwwen the name we are given
#groupdict() -> convert raw data into structure data (dictionary)
#   r'' -> raw Data
#  ?P<timestamp> -> named group
#   s+ -> for spaces one or more
#   ^ -> start of line
#   $ -> end of line
#   \S -> non space character