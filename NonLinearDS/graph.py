from collections import deque

class Vertex:
	def __init__(self, value = None):
		self.value = value
		self.edges = {}


class Graph:
	def __init__(self):
		self.vertices = {}
		self.total_vertices = 0
		self.total_edges = 0

	# Time Complexity: O(1)
	# Auxiliary Space Complexity: O(1) 
	def add_vertex(self, val=None):
		new = Vertex(val)
		if val not in self.vertices:
			self.vertices[val] = new
			self.total_vertices += 1
			# print "added vertex: ", val

	# Time Complexity: O(1)
	# Auxiliary Space Complexity: O(1)
	def get_vertex(self, val):
		if val in self.vertices:
			return self.vertices[val]

	# Time Complexity: O(1)
	# Auxiliary Space Complexity: O(1)
	def add_edge(self, val1, val2):
		if val1 in self.vertices.keys() and val2 in self.vertices.keys():
			v1 = self.vertices[val1]
			v2 = self.vertices[val2]
			v1.edges[val2] = 1
			v2.edges[val1] = 1
			self.total_edges += 1

	# Time Complexity: O(V+E)
	# Auxiliary Space Complexity: O(1)
	def remove_edge(self, val1, val2):
		if val1 in self.vertices.keys() and val2 in self.vertices.keys():
			v1 = self.vertices[val1]
			v2 = self.vertices[val2]
			del v1.edges[val2]
			del v2.edges[val1]
			self.total_edges -= 1

	# Time Complexity: O(1)
	# Auxiliary Space Complexity: O(1)
	def remove_vertex(self, val):
		if val in self.vertices:
			v1 = self.vertices[val]
			for edge in v1.edges.keys():
				self.remove_edge(val, edge)
			del self.vertices[val]
			self.total_vertices -= 1

	# Time Complexity: O(E)
	# Auxiliary Space Complexity: O(1)
	def find_neighbors(self, val):
		if val in self.vertices:
			return self.vertices[val].edges.keys()

	def bfs(self, start):
		visited = []
		q = deque(start)
		while q:
			current = q.popleft()
			if current not in visited:
				visited.append(current)
				for neighbor in self.find_neighbors(current):
					if neighbor not in visited:
						visited.append(neighbor)
						q.append(neighbor)
			print(current, q)
		return visited


g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','D')
print(g.find_neighbors('A'))
print(g.find_neighbors('B'))
print(g.find_neighbors('C'))
print(g.bfs('A'))
