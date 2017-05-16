def quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr)-1]
	left = [x for x in arr if x<pivot]
	middle = [pivot]
	right = [x for x in arr if x>pivot]
	return quicksort(left) + middle + quicksort(right)


print quicksort([4,5,1,3])