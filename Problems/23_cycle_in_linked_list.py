class Node(object):
	def __init__(self, value=None):
		self.value = value
		self.next = None


class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def check_cycle(self):
		current = self.head
		visited = {}
		while current is not None:
			if current.value not in visited:
				visited[current.value] = True
				current = current.next
			else:
				return True
		return False



a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
c.next = a

ll = LinkedList(a)
print ll.check_cycle()
c.next = None
print ll.check_cycle()