'''
Attach additional responsibilities to an object dynamically. Decorators
provide a flexible alternative to subclassing for extending
functionality.
'''

import abc

class Component(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def operation(self):
		pass

class ConcreteComponent(Component):
	def operation(self):
		pass

class Decorator(Component, metaclass=abc.ABCMeta):
	def __init__(self, component):
		self.component = component

	@abc.abstractmethod
	def operation(self):
		pass

class ConcreteDecoratorA(Decorator):
	def operation(self):
		self.component.operation()

class ConcreteDecoratorB(Decorator):
	def operation(self):
		self.component.operation()


def main():
	concrete_decorator_a = ConcreteDecoratorA(ConcreteComponent())
	concrete_decorator_b = ConcreteDecoratorB(concrete_decorator_a)
	concrete_decorator_a.operation()
	concrete_decorator_b.operation()


if __name__ == '__main__':
	main()