class Stack():
	def __init__(self):
		self.storage = []
		# using is a stack to keep track of old max
		self.max = []

	def push(self, value):
		if self.max:
			if value > self.max[-1]:
				self.max.append(value)
		else:
			self.max.append(value)
		self.storage.append(value)

	def pop(self):
		res = self.storage.pop()
		if res == self.max[-1]:
			# we can get old max in O(1)
			self.max.pop()
		return res

	def peek(self):
		return self.storage[-1]

	def get_max(self):
		return self.max[-1]

s = Stack()
s.push(1)
s.push(2)
s.push(10)
s.push(3)
print s.storage
print s.get_max()
s.pop()
s.pop()
print s.storage
print s.get_max()

