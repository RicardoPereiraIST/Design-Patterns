'''
Define the skeleton of an algorithm in an operation, deferring some
steps to subclasses. Template Method lets subclasses redefine certain
steps of an algorithm without changing the algorithm's structure.
'''

import abc

class AbstractClass(metaclass=abc.ABCMeta):
	def template_method(self):
		self.primitive_operation_1()
		self.primitive_operation_2()

	@abc.abstractmethod
	def primitive_operation_1(self):
		pass

	@abc.abstractmethod
	def primitive_operation_2(self):
		pass

class ConcreteClass(AbstractClass):
	def primitive_operation_1(self):
		pass

	def primitive_operation_2(self):
		pass


def main():
	concrete_class = ConcreteClass()
	concrete_class.template_method()

if __name__ == "__main__":
    main()