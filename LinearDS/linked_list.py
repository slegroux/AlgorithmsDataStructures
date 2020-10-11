
class Node(object):
	def __init__(self, value=None):
		self.value = value
		self.next = None


# class LinkedList(object):
# 	def __init__(self, head=None):
# 		self.head = head
# 		self.tail = head
# 		self.length = 0

# 	def __str__(self):
# 		res = []
# 		if self.length == 0:
# 			return
# 		current = self.head
# 		while current != None:
# 			res.append(current.value)
# 			current = current.next
# 		return str(res)

# 	def append(self, value):
# 		# T: O(1)
# 		# S: O(1)

# 		new = Node(value)
# 		if self.length == 0:
# 			self.head = self.tail = new
# 		else:
# 			self.tail.next = new
# 			self.tail = new
# 		self.length += 1

# 	def insert(self, value, index):
# 		# T: O(N)
# 		# S: O(1)

# 		if index < 0 or index >= self.length:
# 			return
# 		new = Node(value)

# 		# list is empty
# 		if self.length == 0:
# 			self.head = self.tail = new

# 		# append at head
# 		elif index == 0:
# 			new.next = self.head
# 			self.head = new

# 		else:
# 			current = self.head
# 			for i in range(index-1):
# 				current = current.next
# 			new.next = current.next
# 			current.next = new

# 		self.length += 1


# 	def remove(self, index):
# 		# T: O(N)
# 		# S: O(1)

# 		if index < 0 or index >= self.length:
# 			return

# 		if self.length == 1:
# 			self.head = self.tail = None

# 		elif index == 0:
# 			self.head = self.head.next
# 		else:
# 			current = self.head
# 			for i in range(index - 1):
# 				current = current.next
# 			current.next = current.next.next
# 			if index == self.length - 1:
# 				self.tail = current
# 		self.length -= 1


class LinkedList():
	def __init__(self):
		self.head = None
	
	def append(self, value):
		if self.head == None:
			self.head = Node(value)
		else:
			current = self.head
			while current.next != None:
				current = current.next
			current.next = Node(value)
	
	def traverse(self):
		current = self.head
		while current != None:
			print(current.value)
			current = current.next

	def prepend(self, value):
		node = Node(value)
		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			self.head = node
	
	def search(self, value):
		current = self.head
		if self.head.value == value:
			return(True)
		else:
			while current != None:
				if current.value == value:
					return(True)
				else:
					current = current.next
			return(False)

	def remove(self, value):
		""" remove first occurence of value """
		# take care of head
		if self.head.value == value:
			self.head = self.head.next
		else:
			current = self.head
			# look one step after head
			while current.next != None:
				if current.next.value == value:
					current.next = current.next.next
				else:
					current = current.next
				
	def to_list(self):
		l = []
		current = self.head
		while current != None:
			l.append(current.value)
			current = current.next
		return(l)


print('append')
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(4)
ll.traverse()
print(ll.to_list())

print("prepend")
ll.prepend(1)
print(ll.to_list())

print("search")
print(ll.search(5))

print("remove") 
ll.remove(2)
ll.traverse()
