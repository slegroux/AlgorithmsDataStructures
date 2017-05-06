# top down
def pow(a, b):
	if b == 0:
		return 1
	if b == 1:
		return a
	return a * pow(a, b - 1)


print pow(2, 3)


# helper version
def pow_(a, b):
	# 1) scope var
	global res
	res = 1
	# 3a) create helper

	def multiply(count):
		global res
		# 4) base case
		if count > b:
			return
		res *= a
		# recursive case
		multiply(count + 1)
	# 3b) invoke helper
	multiply(1)
	# 2) return
	return res

print pow_(2, 3)