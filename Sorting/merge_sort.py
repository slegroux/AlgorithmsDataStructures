def merge(arr1, arr2):
	pt1 = 0
	pt2 = 0



def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	pivot = len(arr) / 2
	left = arr[:pivot]
	right = arr[pivot:]
	sorted_left = merge_sort(left)
	sorted_right = merge_sort(right)

	return merge(sorted_left, sorted_right)

