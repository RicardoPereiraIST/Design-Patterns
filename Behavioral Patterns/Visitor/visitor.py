'''
Represent an operation to be performed on the elements of an object
structure. Visitor lets you define a new operation without changing the
classes of the elements on which it operates.
'''

import abc

class Element(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def accept(self, visitor):
		pass

class ConcreteElementA(Element):
	def accept(self, visitor):
		visitor.visit_concrete_element_a(self)

	def operation_1(self):
		pass

class ConcreteElementB(Element):
	def accept(self, visitor):
		visitor.visit_concrete_element_b(self)

	def operation_2(self):
		pass

class Visitor(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def visit_concrete_element_a(self, element):
		pass

	@abc.abstractmethod
	def visit_concrete_element_b(self, element):
		pass

class ConcreteVisitor1(Visitor):
	def visit_concrete_element_a(self, element):
		pass

	def visit_concrete_element_b(self, element):
		pass

class ConcreteVisitor2(Visitor):
	def visit_concrete_element_a(self, element):
		pass

	def visit_concrete_element_b(self, element):
		pass


def main():
	concrete_visitor_1 = ConcreteVisitor1()
	concrete_element_a = ConcreteElementA()
	concrete_element_a.accept(concrete_visitor_1)	

if __name__ == "__main__":
    main()