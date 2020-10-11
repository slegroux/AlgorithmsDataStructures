#! /usr/bin/env python
from IPython import embed

def binary_search(alist, value):

	first = 0
	last = len(alist) - 1

	while first<=last:
		mid = (first + last) / 2
		if alist[mid] == value:
			return mid
		elif alist[mid] < value:
			first = mid + 1
		else:
			last = mid -1
	return -1

def binary_search_recursive(arr, val):
    pivot = len(arr)//2
    if len(arr) == 1:
        if arr[pivot] != val:
            return(False)

    left = arr[:pivot]
    right = arr[pivot:]
    if val<arr[pivot]:
        return(binary_search_recursive(left, val))
    elif val>arr[pivot]:
        return(binary_search_recursive(right, val))
    elif val == arr[pivot]:
        return(True)

#testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
testlist = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print "binary search: "
print binary_search(testlist, 4)
print binary_search(testlist, 8)
print binary_search(testlist, 0)
print binary_search(testlist, 10)

