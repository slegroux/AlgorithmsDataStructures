#!/usr/bin/env python

# https://www.interviewcake.com/question/python/reverse-linked-list
#

# Hooray! It's opposite day. Linked lists go the opposite way today.
# Write a function for reversing a linked list. Do it in-place.

# Your function will have one input: the head of the list.
# Your function should return the new head of the list.

# IDEA: at each element until we reach the tail, reverse the pointer direction

class Node(object):
	def __init__(self, value):
		self.next = None
		self.value = value

class LinkedList(object):
	def __init__(self):
		self.head = None

	# O(n)
	def append(self, value):
		if self.head == None:
			self.head = Node(value)
		else:
			current = self.head
			while current.next != None:
				current = current.next
			current.next = Node(value)
	
	def remove(self, value):
		if self.head == None:
			return
		else:
			if self.head.value == value:
				self.head = self.head.next
			else:
				current = self.head
				while current.next != None:
					if current.next.value == value:
						current.next = current.next.next
					else:
						current = current.next
				# check last node
				if current.value == value:
					current = None

	def insert(self, value):
		pass

	def print(self):
		res = []
		current = self.head
		res.append(current.value)
		while(current.next != None):
			current = current.next
			res.append(current.value)
		print(res)
	
	def __iter__(self):
		current = self.head
		# note current and not current.next in while loop
		while(current is not None):
			yield current.value
			current = current.next

	def __repr__(self):
		return(str([v for v in self]))

	# O(n)
	def reverse(self):
		if self.head == None:
			return
		else:
			current = self.head
			prev = None
			# keep track of prev and next 
			while current.next != None:
				next = current.next
				current.next = prev
				prev = current
				current = next
			current.next = prev
			self.head = current

if __name__ == "__main__":
	ll = LinkedList()
	ll.append(1)
	ll.append(2)
	ll.append(3)
	ll.append(4)
	# repr
	print(ll)
	ll.print()
	ll.remove(1)
	ll.remove(4)
	print(ll)
	# iterator
	for i in ll:
		print(i)
	ll.reverse()
	print(ll)

