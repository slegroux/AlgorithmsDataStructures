from IPython import embed
from collections import deque

class Node(object):
	def __init__(self, value=None):
		self.value = value
		self.right = None
		self.left = None


class BinarySearchTree(object):
	def __init__(self, root=None):
		self.root = root
		self.size = 0

	def insert(self, value):
		# T: O(log(N))
		# S: O(1)
		new = Node(value)
		if self.root == None:
			self.root = new
			self.size +=1
		else:
			current = self.root
			def traverse(current, new, value):
				if new.value > current.value:
					if current.right:
						traverse(current.right, new, value)
					else:
						current.right = new
						self.size += 1
				elif new.value <= current.value:
					if current.left:
						traverse(current.left, new, value)
					else:
						current.left = new

			traverse(current, new, value)


	def search(self, value):
		current = self.root
		global found
		found = False
		def traverse(current):
			global found
			if current == None:
				return
			if current.value == value:
				found = True
				return 
			elif current.value < value:
				traverse(current.right)
			else:
				traverse(current.left)
		traverse(current)
		return found

	def remove(self):
		pass

	def traverse_in(self):
		# Left-Root-Right
		current = self.root

		def traverse_in_(current):
			if current == None:
				return

			if current.left:
				traverse_in_(current.left)
			print(current.value)
			if current.right:
				traverse_in_(current.right)

		traverse_in_(current)

	def traverse_pre(self):
		# Root-Left-Right
		# check out Node immediately without having seen its children
		current = self.root

		def traverse_pre_(current):
			if current == None:
				return
			print(current.value)
			if current.left:
				traverse_pre_(current.left)
			if current.right:
				traverse_pre_(current.right)
		traverse_pre_(current)

	def traverse_post(self):
		# don't check node until all children have been seen
		# Left-Right-Root
		current = self.root

		def traverse_post_(current):
			if current == None:
				return
			if current.left:
				traverse_post_(current.left)
			if current.right:
				traverse_post_(current.right)
			print(current.value)

		traverse_post_(current)

	def traverse_bfs(self):
		q = deque()
		q.append(self.root)
		while q:
			current = q.popleft()
			print(current.value)
			if current.left:
				q.append(current.left)
			if current.right:
				q.append(current.right)



bst = BinarySearchTree()
#               3
#              / \
#             1   4
#            / \  / \
#                    7
#                     \
#                      11
for value in [3,1,4,7,11]:
	bst.insert(value)

print("in order:")
bst.traverse_in()
print("pre order: ")
bst.traverse_pre()
print("post order: ")
bst.traverse_post()
print("bfs: ")
bst.traverse_bfs()
print(bst.search(4))
print(bst.search(99))