# T: O(N)
# S: O(1)

def reverse(s):
	arr = list(s)
	N = len(arr)
	pt1 = 0
	pt2 = N - 1
	while pt1<pt2:
		arr[pt1], arr[pt2] = arr[pt2], arr[pt1]
		pt1 += 1
		pt2 -= 1
	return ''.join(arr)

# T: O(N)
# S: O(N)
def reverse_recursion(s):
	if len(s) == 0:
		return ""
	def recurse(string, n):
		s = string[:n]
		if n==2:
			return(s[1]+s[0])
		return(s[n-1]+recurse(s,n-1))
	return(recurse(s,len(s)))

print(reverse('abcd'))
print(reverse_recursion('abcd'))