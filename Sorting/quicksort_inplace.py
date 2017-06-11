import sys


def quicksort(arr):
	def divide(start, end):
		if start >= end:
			return

		mid = start
		pivot = end
		for i in range(start, end):
			if arr[i] < arr[pivot]:
				arr[mid], arr[i] = arr[i], arr[mid]
				mid += 1
		arr[mid], arr[pivot] = arr[pivot], arr[mid]
		divide(start, mid-1)
		divide(mid+1, end)
	divide(0, len(arr)-1)
	return arr

print quicksort([4,15,16,50,8,23,42,108])
