import sys

class TempTracker():
	def __init__(self):
		self.min = sys.maxint
		self.max = -sys.maxint
		self.mean = None
		self.count = {}
		self.max_counter = 0
		self.mode = sys.maxint
		self.cum_sum = 0
		self.size = 0

	def get_max(self):
		return self.max

	def get_min(self):
		return self.min

	def get_mean(self):
		return self.mean

	def get_mode(self):
		return self.mode

	def insert(self, val):
		if val in self.count:
			self.count[val] += 1
			if self.count[val] > self.max_counter:
				self.max_counter = self.count[val]
				self.mode = val
		else:
			self.count[val] = 1

		self.cum_sum += val
		self.size += 1
		self.mean = self.cum_sum / float(self.size)
		if val < self.min:
			self.min = val
		if val > self.max:
			self.max = val


t = TempTracker()

for i in [0, 10 , 50 , -3, 10, 0]:
	t.insert(i)

print t.get_max()
print t.get_min()
print t.get_mean()
print t.count
print t.get_mode()
