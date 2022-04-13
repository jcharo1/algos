"""Problem Statement
You have been given an array of length = n. The array contains integers from 0 to n - 2. Each number in the array is present exactly once except for one number which is present twice. Find and return this duplicate number present in the array

Example:

arr = [0, 2, 3, 1, 4, 5, 3]
output = 3 (because 3 is present twice)
The expected time complexity for this problem is O(n) and the expected space-complexity is O(1)."""


arr = [0, 2, 3, 1, 4, 5, 3]
def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    diction= {}
    for key in arr:
        
        if key not in diction:
            diction[key] = 1 
        else:
            diction[key] += 1
    if diction[key] > 1:
        duplicate_number = key
    return duplicate_number

duplicate_number(arr)


def duplicate_number1(arr):
    current_sum=0
    expected_sum=0

    for num in arr:
        current_sum += num
        print(current_sum)
    for i in range(len(arr)-1):
        expected_sum += i
        print(expected_sum)

duplicate_number1(arr)