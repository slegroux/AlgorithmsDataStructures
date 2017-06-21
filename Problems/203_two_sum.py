# Given an array of integers and a target, return a pair of indices 
# where the corresponding values in the array add up to the target.

# Input: Array of Integers, Target Integer
# Output: Two element Array of Integers

# Example
# Input: [1, 6, -5, 7, 3], -2      =>	Output: [2,4]
# Input: [1, 9, 10], 8			=>	Output: [-1,-1]

# Constraints
# Time Complexity: O(N)
# Auxiliary Space Complexity: O(N)

# If the target integer is not found return [-1, -1].
# Values of the array can be positive or negative integers.

def two_sum(arr, target):
	# populate hash with target - elements
	hash = {} 
	for i, el in enumerate(arr):
		hash[el] = i
	# print hash
	for i,el in enumerate(arr):
		if (target - el) in hash:
			return i, hash[target-el]

print two_sum([1, 6, -5, 7, 3], -2)
