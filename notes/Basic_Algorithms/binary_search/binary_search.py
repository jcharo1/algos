'''
In summary:

Binary search is a search algorithm where we find the position of a target value by comparing the middle value with this target value.
If the middle value is equal to the target value, then we have our solution (we have found the position of our target value).
If the target value comes before the middle value, we look for the target value in the left half.
Otherwise, we look for the target value in the right half.
We repeat this process as many times as needed, until we find the target value.

'''
'''
Binary search practice
Let's get some practice doing binary search on an array of integers. We'll solve the problem two different ways—both iteratively and resursively.

Here is a reminder of how the algorithm works:

Find the center of the list (try setting an upper and lower bound to find the center)
Check to see if the element at the center is your target.
If it is, return the index.
If not, is the target greater or less than that element?
If greater, move the lower bound to just above the current center
If less, move the upper bound to just below the current center
Repeat steps 1-6 until you find the target or until the bounds are the same or cross (the upper bound is less than the lower bound).
Problem statement:
Given a sorted array of integers, and a target value, find the index of the target value in the array. If the target value is not present in the array, return -1.

Iterative solution
First, see if you can code an iterative solution (i.e., one that uses loops). If you get stuck, the solution is below.
'''

array = [1,2,3,4,5,6,7,8,9,10]
target = 0
def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration
   
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    
    starting_index = 0
    ending_index = len(array)-1
    while starting_index <= ending_index:
        mid_index = (starting_index + ending_index)//2
        mid_element =array[mid_index]


        if mid_element == target:
            return mid_element
        elif   target > array[mid_index]:
            starting_index = mid_index + 1
        else:
            ending_index = mid_index - 1
    return -1


print(binary_search(array, target))


def binary_search_recursive_soln(array, target, start_index, end_index):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    mid_element = array[mid_index]
    
    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive_soln(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive_soln(array, target, mid_index + 1, end_index)
        
