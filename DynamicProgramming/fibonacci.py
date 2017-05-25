# save intermediate results in hash
def memoize(f):
	memo = {}
	def helper(n):
		if n not in memo:
			memo[n] = f(n)
		return memo[n]
	return helper


# function decorator
@memoize
def fib(n):
	if n <= 1:
		return 1
	return fib(n - 1) + fib(n - 2)


print fib(40)