def parentheses(s, idx):
	# using stack and hash T: O(N), S: O(N)
	l = list(s)
	stack = []
	pair = {}
	for i, el in enumerate(l):
		if el == '(':
			stack.append(i)
		if el == ')':
			pair[stack.pop()] = i
	return pair[idx]

def parentheses_inplace(s, idx):
	l = list(s)
	counter = 1
	pt = idx + 1
	while counter != 0:
		if s[pt] == '(':
			counter += 1
		if s[pt] == ')':
			counter -= 1
		pt += 1
	return pt - 1

print parentheses('Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.', 10)
print parentheses_inplace('Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.', 10)