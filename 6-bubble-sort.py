def bubble_sort(input_list):

    passed = False
    list = input_list
    j = 0
    while j <= (len(list) - 2):
        i = 0
        while i <= (len(list) - 2 - j):
            if list[i] > list[i + 1]:
                passed = True
                list[i], list[i + 1] = list[i + 1], list[i]
            i += 1
        if not passed:
            return input_list
        j += 1
    return(list)


""" my attempt

def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return
"""


list = [45,67,8,58,23,4]
list2 = [0,1,2,3,4,5,6]

print(bubble_sort(list))
print(bubble_sort(list2))