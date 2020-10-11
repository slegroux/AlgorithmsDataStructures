
# flatten([1, [2, 3, [4]], 5, [[6]]]) => [1, 2, 3, 4, 5, 6]

def flatten(arr):
	global res
	res = []
	def traverse(arr):
		if type(arr) == int:
			res.append(arr)
			return
		for el in arr:
			traverse(el)

	traverse(arr)
	return res


print flatten([1, [2, 3, [4]], 5, [[6]]])