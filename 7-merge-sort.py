""" this is my attempt 

def merge(arr_1, arr_2):
    x, y = 0, 0
    fin_arr = []
    while x < len(arr_1) and y < len(arr_2):
        if arr_1[x] > arr_2[y]:
            fin_arr.append(arr_2[y])
            y += 1
        elif arr_1[x] < arr_2[y]:
            fin_arr.append(arr_1[x])
            x += 1
    fin_arr = fin_arr + arr_1[x:] + arr_2[y:]
    return fin_arr


def split(list):
    mid = round(len(list) / 2)
    arr_1 = list[:mid]
    arr_2 = list[mid:]
    return [arr_1, arr_2]


def merge_sort(list):
    x = split(list)
    arr_1 = x[0]
    arr_2 = x[1]
    if len(arr_1) < 1 and len(arr_2) <= 1:
        return [arr_1, arr_2]
    else:
        return (merge(merge_sort(arr_1), merge_sort(arr_2)))
"""


# Python program for implementation of MergeSort
 
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
 
 
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)



# Driver code to test above
arr = [4,6,3,5,1,9,8,2]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i],end=" ")
 
mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i],end=" ")

#list = [4,6,3,5,1,9,8,2]
#print(mergeSort(list))