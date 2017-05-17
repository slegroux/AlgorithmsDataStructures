def insertion_sort(arr):
	# T: O(N^2)
	# S: O(1)
	for i in range(1, len(arr)):
		j = i
		while j > 0 and arr[j] < arr[j - 1]:
			# swap starting from idx
			arr[j], arr[j-1] = arr[j-1], arr[j]
			j = j - 1
	return arr

print(insertion_sort([3, 9, 1, 4, 7]))