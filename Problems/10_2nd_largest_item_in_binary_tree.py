class Node():
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


class BST():
	def __init__(self, root):
		self.root = Node(root)

	def append(self, val):
		new = Node(val)
		current = self.root
		def traverse(current):
			if current.val > new.val:
				if current.left:
					traverse(current.left)
				else:
					current.left = new
			if current.val < new.val:
				if current.right:
					traverse(current.right)
				else:
					current.right = new
		traverse(current)

	def in_order(self):
		current = self.root
		def traverse(current):
			if current == None:
				return
			if current.left:
				traverse(current.left)
			print current.val
			if current.right:
				traverse(current.right)
		traverse(current)

	def largest(self, current):
		# node at the far right
		# current = self.root
		def traverse(current):
			if current.right:
				traverse(current.right)
			else:
				traverse.res = current.val
		traverse.res = None
		traverse(current)
		return traverse.res

	def second_largest(self):
		# wether there is a left subtree or not
		current = self.root

		def traverse(current):
			if current.left and not current.right:
				traverse.res = self.largest(current.left)
			if current.right and not current.right.right and not current.right.left:
				traverse.res = current.right.val
			if current.right:
				traverse(current.right)

		traverse.res = None
		traverse(current)
		return traverse.res




t = BST(4)
t.append(2)
t.append(15)
t.append(20)
t.append(16)
t.append(17)
from pprint import pprint
pprint(t)
print t.in_order()
print t.largest(t.root)
print t.second_largest()