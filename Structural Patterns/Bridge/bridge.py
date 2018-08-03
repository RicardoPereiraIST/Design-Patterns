'''
Decouple an abstraction from its implementation so that the two can vary
independently.
'''

import abc

class Abstraction:
	def __init__(self, implementor):
		self.implementor = implementor

	def function(self):
		self.implementor.implementation()

class ConcreteAbstractionA(Abstraction):
	def refined_function(self):
		pass

class ConcreteAbstractionB(Abstraction):
	def refined_function(self):
		pass

class Implementor(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def implementation(self):
		pass

class ConcreteImplementorA(Implementor):
	def implementation(self):
		pass

class ConcreteImplementorB(Implementor):
	def implementation(self):
		pass


def main():
	for implementor in (ConcreteImplementorA(), ConcreteImplementorB()):
		for abstraction in (ConcreteAbstractionA(implementor), ConcreteAbstractionB(implementor)):
			abstraction.function()


if __name__ == '__main__':
	main()