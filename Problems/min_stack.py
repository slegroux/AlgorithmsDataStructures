# Design a min stack class with the following methods:
# push(value) - Push an integer onto the stack.
# pop() - Removes and returns the element on top of the stack
# peek() - Return the top value in the stack (do not remove it)
# min() - Return the minimum value in the stack

# Input: N/A
# Output: Instance of a min stack

class min_stack(object):
	def __init__(self):
		self.min = None
		self.data = []

	def push(self, value):
		self.data.append(value)
		self.min = min(self.data)

	def pop(self):
		res = self.data.pop()
		self.min = min(self.data)
		return res

	def peek(self):
		return self.data[len(self.data)-1]

	def min(self):
		return self.min


s = min_stack()
s.push(5)
print s.min
s.push(3)
s.push(10)
print s.data
print "min ", s.min
print s.pop()
print s.peek()
print s.pop()
print s.data