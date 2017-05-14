
class Node(object):
	def __init__(self, value=None):
		self.value = value
		self.next = None


class LinkedList(object):
	def __init__(self, head=None):
		self.head = head
		self.tail = head
		self.length = 0

	def __str__(self):
		res = []
		if self.length == 0:
			return
		current = self.head
		while current != None:
			res.append(current.value)
			current = current.next
		return str(res)

	def append(self, value):
		new = Node(value)
		if self.length == 0:
			self.head = self.tail = new
		else:
			self.tail.next = new
			self.tail = new
		self.length += 1

	def insert(self, value, index):
		if index < 0 or index >= self.length:
			return
		new = Node(value)

		# list is empty
		if self.length == 0:
			self.head = self.tail = new

		# append at head
		elif index == 0:
			new.next = self.head
			self.head = new

		else:
			current = self.head
			for i in range(index-1):
				current = current.next
			new.next = current.next
			current.next = new

		self.length += 1


	def remove(self, index):
		if index < 0 or index >= self.length:
			return

		if self.length == 1:
			self.head = self.tail = None

		elif index == 0:
			self.head = self.head.next
		else:
			current = self.head
			for i in range(index - 1):
				current = current.next
			current.next = current.next.next
			if index == self.length-1:
				self.tail = current
		self.length -= 1


ll = LinkedList()
print "append from None"
ll.append(0)
ll.append(1)
ll.append(10)
print "insert at head"
print ll
ll.insert(5, 0)
print ll
ll.insert(5, 3)
print ll
ll.append(100)
print ll
ll.remove(5)
print ll
ll.remove(0)
print ll
ll.remove(2)
print ll

