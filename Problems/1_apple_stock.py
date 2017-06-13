def max_profit(arr):
	minimum = arr[0]
	profit = 0
	for i in range(1, len(arr)):
		if arr[i] - minimum > profit:
			profit = (arr[i] - minimum)
		if arr[i] < minimum:
			minimum = arr[i]
	return profit

print max_profit([10, 7, 5, 8, 11, 9])