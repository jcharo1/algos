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
    
    return print(f"First record of texts, {textIncomingNumber} texts {textAnsweringNumber} at time {textTime} \nLast record of calls, {callsIncomingNumber} calls {callsAnsweringNumber} at time {callsTime}, lasting {callsDuration} seconds")
        
        
# getFirstgetLast()


# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# for name in names:
#     name = name.lower().replace(" ", "_")
#     print(name)
# print(names)



# # number we'll find the factorial of
# number = 6
# # start with our product equal to one
# product = 1

# # calculate factorial of number with a for loop
# for num in range(2, number + 1):
#     product *= num
#     print(num, product)
# # print the factorial of number
# print(product)


# check_prime = [26, 39, 51, 53, 57, 79, 85]

# # iterate through the check_prime list
# for num in check_prime:

# # search for factors, iterating through numbers ranging from 2 to the number itself
#     for i in range(2, num):

# # number is not prime if modulo is 0
#         if (num % i) == 0:
#             print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
#             break

# # otherwise keep checking until we've searched all possible factors, and then declare it prime
#         if i == num -1:    
#             print("{} IS a prime number".format(num))
