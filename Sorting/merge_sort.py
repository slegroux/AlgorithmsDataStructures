def merge(arr1, arr2):
	n1 = len(arr1)
	n2 = len(arr2)
	pt1 = 0
	pt2 = 0
	res = []
	while pt1 < n1 and pt2 < n2:
		if arr1[pt1] < arr2[pt2]:
			res.append(arr1[pt1])
			pt1 += 1
		else:
			res.append(arr2[pt2])
			pt2 += 1
	# if we reached the end of arr1
	if pt1 == n1:
		while pt2 < n2:
			res.append(arr2[pt2])
			pt2 += 1
	# else we reached the end of arr2
	else:
		while pt1<n1:
			res.append(arr1[pt1])
			pt1 += 1

	return res


def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	pivot = len(arr) / 2
	left = arr[:pivot]
	right = arr[pivot:]
	sorted_left = merge_sort(left)
	sorted_right = merge_sort(right)

	return merge(sorted_left, sorted_right)


print merge([1,4,5], [2,6,7])
print merge_sort([10,2,4,6,11,0])