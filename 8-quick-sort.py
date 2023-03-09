"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
#https://www.youtube.com/watch?v=0SkOjNaO1XY&t=222s

def quicksort(arr):
    qs(arr, 0, len(arr) - 1)

def qs(arr, l, r):
    if l >= r:
        return
    p = partition(arr, l, r)

    qs(arr, l, p - 1)
    qs(arr, p + 1, r)

def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1




test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
quicksort(test)
print(test) 