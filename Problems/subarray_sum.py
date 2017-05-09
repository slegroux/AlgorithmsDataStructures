# Given an array of positive integers and a target value, return true if there is a subarray of consecutive elements that sum up to this target value. 

# Input: Array of integers, target value
# Output: Boolean

# Example
# Input: [6,12,1,7,5,2,3], 14      	=>	Output: true (7+5+2)
# Input: [8,3,7,9,10,1,13], 50		=>	Output: false

# Constraints
# Time Complexity: O(N)
# Auxiliary Space Complexity: O(1)
# All elements are positive


def subarray_sum(arr, target):
	start = 0
	current = 0
	sum = arr[start]

	while start < len(arr) - 1 and current < len(arr):
		print start, current, sum
		if sum == target:
			return True
		else:
			if sum > target:
				start += 1
				current = start
				sum = arr[start]
			else:
				current += 1
				sum += arr[current]
				print sum
	return False


print subarray_sum([6, 12, 1, 7, 5, 2, 3], 14)
print subarray_sum([2, 5], 7)
print subarray_sum([7], 7)