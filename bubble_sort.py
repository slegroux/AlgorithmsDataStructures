def bubble_sort(arr):
	# T: O(N**2)
	# S: O(1)
	for j in range(len(arr)):
		for i in range(len(arr) - j - 1):
			if arr[i+1] < arr[i]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
	return arr


print(bubble_sort([3,9,1,4,7]))