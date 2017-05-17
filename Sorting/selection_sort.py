import sys

def minimum(arr):
	m = sys.maxint
	m_i = 0
	for i, item in enumerate(arr):
		if item < m:
			m = item
			m_i = i
	return m, m_i

def selection_sort(arr):
	for i in range(1, len(arr)):
		m, m_i = minimum(arr[i:len(arr)])
		# don't forget to add +i index (since we compute maximum on the sliced array)
		arr[i-1], arr[m_i+i] = arr[m_i+i], arr[i-1]
		# print m, m_i, arr

	return arr

print(selection_sort([3,9,1,4,7]))