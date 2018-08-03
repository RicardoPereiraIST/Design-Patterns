'''
Separate the construction of a complex object from its representation so
that the same construction process can create different representations.
'''

import abc

class Director:
	def __init__(self):
		self.builder = None

	def construct(self, builder):
		self.builder = builder
		self.builder.build_part_a()
		self.builder.build_part_b()
		self.builder.build_part_c()

class Builder(metaclass=abc.ABCMeta):
	def __init__(self):
		self.product = Product()

	@abc.abstractmethod
	def build_part_a(self):
		pass

	@abc.abstractmethod
	def build_part_b(self):
		pass
	
	@abc.abstractmethod
	def build_part_c(self):
		pass	

class ConcreteBuilder(Builder):
	def build_part_a(self):
		pass

	def build_part_b(self):
		pass
		
	def build_part_c(self):
		pass

class Product:
	pass


def main():
	director = Director()
	concrete_builder = ConcreteBuilder()
	director.construct(concrete_builder)
	product = concrete_builder.product

if __name__ == '__main__':
	main()