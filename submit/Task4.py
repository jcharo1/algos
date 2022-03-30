"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def list_of_telemarketers(calls):
    callers = []
    possible_telemarketer=[]
    verified_not_telemarketers=[]
    for phone_number in calls:
        callers.append(phone_number[0])
        verified_not_telemarketers.append(phone_number[1])
    for phone_number in texts:
        verified_not_telemarketers.append(phone_number[0])
        verified_not_telemarketers.append(phone_number[1])

    for phone_number in callers:
        if phone_number not in verified_not_telemarketers:
            possible_telemarketer.append(phone_number)
    return possible_telemarketer

def ordered_no_duplicate_list(unordered_list):
  print("These numbers could be telemarketers: ")
  new_set = set(unordered_list)
  sorted_unique_numbers =sorted(new_set)
  for phone_number in sorted_unique_numbers:
    print (phone_number)


possible_telemarketer_numbers = list_of_telemarketers(calls)

ordered_no_duplicate_list(possible_telemarketer_numbers)
