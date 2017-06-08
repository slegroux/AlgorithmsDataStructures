class Node:
	def __init__(self, value=None):
		self.value = value
		self.next = None


class LinkedList():
	def __init__(self, head=None):
		head = Node(head)
		self.head = head
		if head:
			self.length = 1
		else:
			self.length = 0

	def append(self, value):
		new = Node(value)
		current = self.head
		while current.next is not None:
			current = current.next
		current.next = new
		self.length += 1

	def print_list(self):
		print "length: ", self.length
		current = self.head
		while current!=None:
			print current.value
			current = current.next

	def kth_to_last(self, k):
		# somewhat inefficient
		current = self.head
		counter = 0
		if k > self.length:
			return

		if current is not None:
			while counter < self.length - k:
				current = current.next
				counter += 1
		return current.value

	def kth_to_last_(self, k):
		# k length "stick" trick
		pt_l = self.head
		pt_r = self.head
		counter = 0
		while counter < k:
			counter += 1
			pt_r = pt_r.next

		while pt_r is not None:
			pt_r = pt_r.next
			pt_l = pt_l.next
		return pt_l.value


ll = LinkedList('a')
ll.append('b')
ll.append('c')
ll.append('d')
ll.print_list()
print ll.kth_to_last(3)
print ll.kth_to_last(1)
print ll.kth_to_last_(3)
print ll.kth_to_last_(1)
