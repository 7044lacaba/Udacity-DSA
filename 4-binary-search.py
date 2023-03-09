"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    """Your code goes here."""

    low = 0
    high = len(input_array) - 1 
    mid = 0

    while low <= high:
        mid = round((low + high) / 2)
        if value > input_array[mid]:
            low = mid + 1
        elif value < input_array[mid]:
            high = mid - 1
        else:
            return mid
    else:
        return -1

    """ my attempt
    
    array = input_array
    try:
        for item in array:
            range_mid = half_round_up(len(array))
            if array == []:
                break
            else:
                if value == array[range_mid]:
                    return input_array.index(value)                
                elif value > array[range_mid]:
                    array = array[range_mid:]
                elif value < array[range_mid]:
                    array = array[0:range_mid]
    except: 
        return -1
    """



test_list = [0,1,2,3,4,5,6]
test_val1 = 0
test_val2 = 1
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))