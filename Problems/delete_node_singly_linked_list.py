import inspect

class Node():
	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList():
	def __init__(self, head):
		head = Node(head)
		self.head = head

	def append(self, value):
		new = Node(value)
		current = self.head
		while current.next is not None:
			current = current.next
		current.next = new

	def print_list(self):
		res = []
		current = self.head
		while current is not None:
			res.append(current.value)
			current = current.next
		print res

	def get_node(self, index):
		# T: O(N), S: O(1)
		count = 0
		current = self.head
		while count < index:
			current = current.next
			count += 1
		return current

	def delete(self, index):
		# t: O(1), S: O(1)
		current = self.get_node(index)
		next = current.next
		current.value = next.value
		current.next = next.next

ll = LinkedList('1')
ll.append(2)
ll.append(3)
ll.append(4)
print ll.__dict__
ll.print_list()

print ll.get_node(2).value

ll.delete(2)
ll.print_list()

# doesn't work for last node