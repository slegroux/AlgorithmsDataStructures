# top down, no helper function
def factorial(n):
	# base case
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n - 1)


print factorial(3)

# bottom up, helper function
# 1. instantiate scope variables
# 2. return result
# 3. a) create helper method
#    b) invoke helper method
# 4. base case
# 5. recursive case

def factorial_(n):
	global res
	res = 1
	def multiply(count):
		global res
		if count>n:
			return
		res *= count
		multiply(count + 1)
	multiply(1)
	return res

print factorial_(3)