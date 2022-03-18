"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from enum import unique
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""




def total_unique_numbers():
    unique_phone_numbers={}

    for text in texts:
    
        unique_phone_numbers[text[0]] = text[0]
        unique_phone_numbers[text[1]] = text[1]
    
    for call in calls:
        unique_phone_numbers[call[0]] = call[0]
        unique_phone_numbers[call[1]] = call[1]   
    
    total = len(unique_phone_numbers.keys())
    return print(f"There are {total} different telephone numbers in the records.")


total_unique_numbers()


"""Big O
The runtime of this algorithm is O(n) or linear, Worst case would be O((n+n)+2)
"""
  
  