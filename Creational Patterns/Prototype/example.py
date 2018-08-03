import abc
import copy

class Person(metaclass=abc.ABCMeta):
	def __init__(self, name):
		self.name = name

	@abc.abstractmethod
	def clone(self):
		pass

class Tom(Person):
	def __init__(self):
		self.name = "Tom"

	def clone(self):
		return Tom()

class John(Person):
	def __init__(self):
		self.name = "John"

	def clone(self):
		return John()

class Harry(Person):
	def __init__(self):
		self.name = "Harry"

	def clone(self):
		return Harry()

class Factory:
	prototypes = {"Tom" : Tom(), "John" : John(), "Harry" : Harry()}

	def get_prototype(self, name):
		if name in self.prototypes.keys():
			return self.prototypes[name].clone()
		else:
			print("Prototype with name " + name + " does not exist.")


def main():
	factory = Factory()

	for name in ["Tom", "John", "Harry", "Sam"]:
		person = factory.get_prototype(name)
		if person:
			print(person.name)

	#Using copy
	john = copy.deepcopy(factory.get_prototype("Tom"))
	print(john.name)
	john.name = "John"
	print(john.name)

if __name__ == '__main__':
	main()