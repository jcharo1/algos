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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
def getFirstgetLast():
    textIncomingNumber = texts[0][0]
    textAnsweringNumber = texts[0][1]
    textTime = texts[0][2]
    callsIncomingNumber = calls[-1][0]
    callsAnsweringNumber = calls[-1][1]
    callsTime = calls[-1][2]
    callsDuration = calls[-1][3]
    print(texts[0])
    return print(f"First record of texts, {textIncomingNumber} texts {textAnsweringNumber} at time {textTime} \nLast record of calls, {callsIncomingNumber} calls {callsAnsweringNumber} at time {callsTime}, lasting {callsDuration} seconds")
        
        
getFirstgetLast()


"""Big O
The runtime of this algorithm is constant which would be O(1), Worst case would be the same as it is constant
"""