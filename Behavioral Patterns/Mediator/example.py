class Node:
	def __init__(self, v):
		self.value = v

class List:
	def __init__(self):
		self.arr = []

	def add_node(self, node):
		self.arr.append(node)

	def traverse(self):
		for i in self.arr:
			print(i.value, end='	', flush=True)
		print()

	def remove_node(self, value):
		size = len(self.arr)
		for i in range(size):
			if self.arr[i].value == value:
				self.arr.pop(i)
				break

def main():
	lst = List()
	one, two, three, four = Node(11), Node(22), Node(33), Node(44)
	lst.add_node(one)
	lst.add_node(two)
	lst.add_node(three)
	lst.add_node(four)
	lst.traverse()
	lst.remove_node(44)
	lst.traverse()
	lst.remove_node(22)
	lst.traverse()
	lst.remove_node(11)
	lst.traverse()

if __name__ == "__main__":
    main()