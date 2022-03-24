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
    telemarketer_nums = []
    for x in calls:
        if x[0].startswith("140"):
            telemarketer_nums.append(x[0])
    return telemarketer_nums


def ordered_no_dup_list(unordered_list):
  print("These numbers could be telemarketers: ")
  se = set(unordered_list)
  sorted_unique_numbers =sorted(se)
  for x in sorted_unique_numbers:
    print (x)


xx = list_of_telemarketers(calls)
ordered_no_dup_list(xx)
