def bracket_validator(s):
	l = list(s)
	stack = []
	openers = ['(', '{', '[']
	closers = [')', '}', ']' ]
	h = {}
	for i, el in enumerate(closers):
		h[el] = openers[i]

	for el in l:
		if el in openers:
			stack.append(el)
		if el in closers:
			if stack.pop() != h[el]:
				return False
	return True




print bracket_validator("{ [ ] ( ) }")
print bracket_validator("{ [ ( ] ) }")
print bracket_validator("{ [ }")