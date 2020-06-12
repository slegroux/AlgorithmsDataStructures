
# this problem is from
# https://www.interviewcake.com/question/python/linked-list-cycles
#

# You have a singly-linked list and want to check if it contains a cycle.

# A singly-linked list is built with nodes, where each node has:

# node.next -- the next node in the list.

# node.value -- the data held in the node. For example, if our linked
# list stores people in line at the movies, node.value might be the
# person's name.

# For example:


class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

# A cycle occurs when a node's next points back to a previous node in
# the list. The linked list is no longer linear with a beginning and
# end -- instead, it cycles through a loop of nodes.

# Write a function contains_cycle() that takes the first node in a
# singly-linked list and returns a boolean indicating whether the list
# contains a cycle.


class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList(object):
	def __init__(self, init_list = None):
		self.head = None
		if init_list:
			for value in init_list:
				self.append(value)

	def append(self, value):
		if self.head == None:
			self.head = Node(value)
		else:
			current = self.head
			while current.next != None:
				current = current.next
			current.next = Node(value)

	def check_values(self):
		current = self.head
		visited = {}
		while current is not None:
			if current.value not in visited:
				visited[current.value] = True
				current = current.next
			else:
				return True
		return False

	# use 2 runners 1 slow and one faster. there is a loop if the fastest one catches the slower one
	def is_circular(self):
		if self.head == None:
			return False

		fast = self.head
		slow = self.head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
			if slow == fast:
				return(True)
		return(False)
			

ll = LinkedList([2, -1, 3, 0, 5])
# start cycle node
cycle_start = ll.head.next
# loop back last node to start
current = ll.head
while current.next:
	current = current.next
current.next = cycle_start

ll2 = LinkedList([2, -1, 3, 0, 5, 10, 20])
print(ll.is_circular())
print(ll2.is_circular())