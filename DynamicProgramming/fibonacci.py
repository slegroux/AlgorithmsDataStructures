# save intermediate results in hash
def memoize(f):
	memo = {}
	def helper(n):
		if n not in memo:
			memo[n] = f(n)
		return memo[n]
	return helper


# function decorator
# memoization converts O(2^n) recursive calls into O(n) hash indexing
@memoize
def fib(n):
	if n <= 1:
		return 1
	return fib(n - 1) + fib(n - 2)



def fib_mem(n):
	global memo
	memo = {}
	def helper(n):
		global memo
		if n<=1:
			return 1
		if n not in memo:
			memo[n] = helper(n-1) + helper(n-2)
		return memo[n]
	helper(n)
	return memo[n]

print fib(40)
print fib_mem(40)
