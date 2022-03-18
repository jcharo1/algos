"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from audioop import findmax
import csv
from re import X

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def findMaximum(call_duration_dict):        
    max = None
    max_key = None
    for key, value in call_duration_dict.items():
        if not max:
            max = value
            max_key = key
        elif max < value:
            max = value
            max_key = key
    return print(f"{max_key} spent the longest time, {max} seconds, on the phone during September 2016.")

def total_unique_numbers(find_unique_calls):
    unique_phone_numbers={}
    for call in find_unique_calls:
        if call[0] not in unique_phone_numbers:
            unique_phone_numbers[call[0]] = 0
        if call[1] not in unique_phone_numbers:
            unique_phone_numbers[call[1]] = 0
        unique_phone_numbers[call[0]] += int(call[3])
        unique_phone_numbers[call[1]] += int(call[3])   


    
    return unique_phone_numbers

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


uniqueNumberDuration = total_unique_numbers(calls)

findMaximum(uniqueNumberDuration)
