
def merge_meeting(arr):
	N = len(arr)
	result = []
	# we hypothesize pairs sorted by start time so start1<start2
	i = 0
	while i < N - 1:
		start1 = arr[i][0]
		end1 = arr[i][1]
		start2 = arr[i+1][0]
		end2 = arr[i+1][1]
		print start1, end1, start2, end2
		if start2 <= end1:
			if end2 > end1:
				pair = (start1, end2)
			if end2 < end1:
				pair = (start1, end1)
			result.append(pair)
			i += 2
		else:
			result.append(arr[i])
			i += 1

	return result









# first sort meetings by start date
print merge_meeting([(0, 1), (3, 5), (4, 8), (9, 10),(10, 12)])
print merge_meeting([(1, 10), (2, 6), (3, 5), (7, 9)])
print merge_meeting(  [(1, 5), (2, 3)])