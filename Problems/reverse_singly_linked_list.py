# IDEA: at each element until we reach the tail, reverse the pointer direction
class Node(object):
	def __init__(self, value = None):
		self.next = None
		self.value = value

class LinkedList(object):
	def __init__(self, head = None):
		self.head = head

	def append(self, value):
		current = self.head
		n = Node(value)
		if current == None:
			self.head = n
		else:
			while current.next != None:
				current = current.next
			current.next = n

	def print_list(self):
		res = []
		current = self.head
		while(current != None):
			res.append(current.value)
			current = current.next
		print res

	def reverse(self):
		prev = None
		current = self.head
		while current != None:
			# copy next node
			next = current.next
			# reverse pointer direction for current
			current.next = prev
			# move forward in linked list
			prev = current
			current = next
		self.head = prev




ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()
ll.reverse()
ll.print_list()