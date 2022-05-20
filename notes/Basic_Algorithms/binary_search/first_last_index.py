'''## Problem statement

Given a sorted array that may have duplicate values, use *binary search* to find the **first** and **last** indexes of a given value.

For example, if you have the array `[0, 1, 2, 2, 3, 3, 3, 4, 5, 6]` and the given value is `3`, the answer will be `[4, 6]` (because the value `3` occurs first at index `4` and last at index `6` in the array).

The expected complexity of the problem is $O(log(n))$.'''
arr = [0, 1, 2, 2, 3, 3, 3, 4, 5, 6]
target = 3

def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary 
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """
        
    # TODO: Write your first_and_last function here
    # Note that you may want to write helper functions to find the start 
    # index and the end index
    first = find_first(arr,number)
    last = find_last(arr,number)
    f_l_indicies = [first,last]
    return f_l_indicies

    
           
def binary_search(arr,number):
    if len(arr)==0:
        return -1
    start_index = 0
    end_index = len(arr)-1
    while start_index <= end_index:
        mid_index= (start_index + end_index)//2
        mid_element = arr[mid_index]
        if number == mid_element:
            return mid_index
        elif number < mid_element:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1
    return -1

def find_first(arr,target):
    index = binary_search(arr,target)
    if index == -1:
        return -1
    while arr[index]==target:
        if index == 0:
            return 0
        if arr[index-1]==target:
            index -= 1
        else:
            return index
def find_last(arr,target):
    index = binary_search(arr,target)
    
    if index == -1:
        return -1
    while arr[index]==target:
        if index == len(arr)-1:
            return index
        if arr[index+1]==target:
            index += 1
        else:
            return index




arr = [1,3]
target =0


def searchInsert(nums, target):
      
        start_index = 0
        end_index = len(nums)-1
        
        while start_index <= end_index:
            mid_index = (start_index+end_index) //2
            mid_element = nums[mid_index]
            print(f'''start_index : {start_index}
            end_index {end_index}
            mid_index {mid_index}''')

            if start_index ==mid_index:
                print("i made it here")
                if target == 0:
                    return 0 
                if target<nums[start_index]:
                    return start_index -1
                if target>nums[start_index]:
                    return start_index + 1
            if mid_element == target:
                return mid_index
            elif target < mid_element:
                end_index = mid_index -1
            else:
                start_index = mid_index+1

print(searchInsert(arr,target))
