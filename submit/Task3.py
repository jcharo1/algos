import re
import json
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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""


def area_codes_called_by_bangalore(calls):
  called_from_bangaloreList = []


  for x in calls:
      if x[0].startswith('(080)'):
          if x[1].startswith('('):
              x[1] = re.search(r'^\((0+\d*)\)', x[1]).group(0)
              called_from_bangaloreList.append(x[1])
          if x[1].startswith(("7", '8', '9')):

              called_from_bangaloreList.append(x[1][0:4])
          if x[1].startswith("140"):
              x[1] = "140"
              called_from_bangaloreList.append(x[1])

  
  return called_from_bangaloreList
    

def ordered_no_duplicate_list(unordered_list):
  print("The numbers called by people in Bangalore have codes:")
  new_set = set(unordered_list)
  sorted_unique_area_codes =sorted(new_set)
  for area_code in sorted_unique_area_codes:
    print (area_code)

area_codes_called_by_bangalore = area_codes_called_by_bangalore(calls)
ordered_no_duplicate_list(area_codes_called_by_bangalore)



"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""



def percentage_of_calls(calls):
  total_calls_in_banglore  = []

  calls_in_banglore  = []
  for x in calls:
      if x[0].startswith('(080)'):
        calls_in_banglore.append(x[1])
        if x[1].startswith('(080)'):
          total_calls_in_banglore.append(x[1])
  

  percentage = len(total_calls_in_banglore) / len(calls_in_banglore) * 100
  format_percentage = "{:.2f}".format(percentage)
  return print(f"{format_percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
  



percentage_of_calls(calls)

