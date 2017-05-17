#! /usr/bin/env python


# O(n)
def sequentialSearch(alist, item):
	res = None
	for i in range(len(alist)):
		if alist[i] == item:
			res = i
	return res


def sentinelSearch(alist, item):
	tmp = alist[len(alist) - 1]
	alist[len(alist) - 1] = item
	i = 0
	while alist[i] != item:
		i += 1
	alist[len(alist) - 1] = tmp
	if i < len(alist) or alist[len(alist) - 1] == item:
		return i
	else:
		return -1


def recursive_linear_search(alist, item):
	pass


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print sequentialSearch(testlist, 17)
print sequentialSearch(testlist, 0)
print sequentialSearch(testlist, 1)
print sentinelSearch(testlist, 17)
