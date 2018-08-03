'''
Compose objects into tree structures to represent part-whole
hierarchies. Composite lets clients treat individual objects and
compositions of objects uniformly.
'''

import abc

class Component(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def operation(self):
		pass

class Composite(Component):
	def __init__(self):
		self.components = set()

	def operation(self):
		for component in self.components:
			component.operation()

	def add(self, component):
		self.components.add(component)

	def remove(self, component):
		self.components.discard(component)

class Leaf(Component):
	def operation(self):
		pass


def main():
	composite = Composite()
	leaf = Leaf()
	composite.add(leaf)
	composite.operation()
	composite.remove(leaf)


if __name__ == '__main__':
	main()