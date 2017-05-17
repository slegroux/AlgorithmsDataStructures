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


#testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
testlist = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print "binary search: "
print binary_search(testlist, 4)
print binary_search(testlist, 8)
print binary_search(testlist, 0)
print binary_search(testlist, 10)

