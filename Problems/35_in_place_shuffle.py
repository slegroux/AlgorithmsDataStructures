from random import randint


def shuffle_rep(arr):
	# not in place and replacement
	res = []
	N = len(arr)
	for i in range(N):
		rand_idx = randint(0, N - 1)
		res.append(arr[rand_idx])
	return res


def shuffle_norep(arr):
	# not in place and no replacement
	res = []
	while len(arr) > 0:
		rand_idx = randint(0, len(arr) - 1)
		res.append(arr[rand_idx])
		del arr[rand_idx]
	return res


def shuffle_in_place(arr):
	N = len(arr)
	for i in range(N):
		idx = randint(i, N - 1)
		arr[i], arr[idx] = arr[idx], arr[i]
	return arr



print "Replacement:"
for i in range(5):
	print shuffle_rep([4, 5, 3, 1, 7])

print "No Replacement:"
for i in range(5):
	print shuffle_norep([4, 5, 3, 1, 7])

print "No Replacement in place"
h = {}
for i in range(10000):
	res = shuffle_in_place([4, 5, 3, 1, 7])
	if res[0] not in h:
		h[res[0]] = 1
	else:
		h[res[0]] += 1
print h
