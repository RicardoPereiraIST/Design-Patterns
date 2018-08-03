import abc

class Component(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def traverse(self):
		pass

class Composite(Component):
	def __init__(self):
		self.components = []

	def traverse(self):
		for component in self.components:
			component.traverse()

	def add(self, component):
		self.components.append(component)

	def remove(self, component):
		self.components.remove(component)

class Leaf(Component):
	def __init__(self, value):
		self.value = value

	def traverse(self):
		print(self.value, end = ' ', flush = True)


def main():
	composite = [Composite() for _ in range(4)]
	
	for i in range(4):
		for j in range(3):
			composite[i].add(Leaf(i * 3 + j))

	for i in range(1, 4, 1):
		composite[0].add(composite[i])

	for i in range(4):
		composite[i].traverse()
		print()


if __name__ == '__main__':
	main()