'''
Define an interface for creating an object, but let subclasses decide
which class to instantiate. Factory Method lets a class defer
instantiation to subclasses.
'''

import abc

class Creator(metaclass=abc.ABCMeta):
	def __init__(self):
		self.product = self.factory_method()

	@abc.abstractmethod
	def factory_method(self):
		pass

	def operation(self):
		self.product.interface()


class ConcreteCreator1(Creator):
	def factory_method(self):
		return ConcreteProduct1()


class ConcreteCreator2(Creator):
	def factory_method(self):
		return ConcreteProduct2()


class Product(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def interface(self):
		pass


class ConcreteProduct1(Product):
	def interface(self):
		pass


class ConcreteProduct2(Product):
	def interface(self):
		pass


def main():
	for concrete_creator in (ConcreteCreator1(), ConcreteCreator2()):
		concrete_creator.product.interface()
		concrete_creator.operation()

if __name__ == '__main__':
	main()