def reverse(s):
	arr = list(s)
	N = len(arr)
	pt1 = 0
	pt2 = N - 1
	while pt2 > pt1:
		arr[pt1], arr[pt2] = arr[pt2], arr[pt1]
		pt1 += 1
		pt2 -= 1
	return ''.join(arr)


print reverse('abcd')
