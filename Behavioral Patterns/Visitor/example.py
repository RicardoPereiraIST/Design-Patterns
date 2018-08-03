import abc

class Element(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def accept(self, visitor):
		pass

class FOO(Element):
	def accept(self, visitor):
		visitor.visit_foo(self)

	def get_foo(self):
		return "FOO"

class BAR(Element):
	def accept(self, visitor):
		visitor.visit_bar(self)

	def get_bar(self):
		return "BAR"

class BAZ(Element):
	def accept(self, visitor):
		visitor.visit_baz(self)

	def get_baz(self):
		return "BAZ"

class Visitor(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def visit_foo(self, element):
		pass

	@abc.abstractmethod
	def visit_bar(self, element):
		pass

	@abc.abstractmethod
	def visit_baz(self, element):
		pass

class UpVisitor(Visitor):
	def visit_foo(self, element):
		print("Do Up on " + element.get_foo())

	def visit_bar(self, element):
		print("Do Up on " + element.get_bar())

	def visit_baz(self, element):
		print("Do Up on " + element.get_baz())

class DownVisitor(Visitor):
	def visit_foo(self, element):
		print("Do Down on " + element.get_foo())

	def visit_bar(self, element):
		print("Do Down on " + element.get_bar())

	def visit_baz(self, element):
		print("Do Down on " + element.get_baz())

def main():
	elements = [FOO(), BAR(), BAZ()]
	up, down = UpVisitor(), DownVisitor()
	[element.accept(up) for element in elements]
	[element.accept(down) for element in elements]

if __name__ == "__main__":
    main()