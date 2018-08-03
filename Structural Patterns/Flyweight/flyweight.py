'''
Use sharing to support large numbers of fine-grained objects
efficiently.
'''

import abc

class FlyweightFactory:
	def __init__(self):
		self.flyweights = {}

	def get_flyweight_key(self, key):
		try:
			flyweight = self.flyweights[key]
		except:
			flyweight = ConcreteFlyweight()
			self.flyweights[key] = flyweight

		return flyweight


class Flyweight(metaclass=abc.ABCMeta):
	def __init__(self):
		self.intrinsic_state = None

	@abc.abstractmethod
	def operation(self, extrinsic_state):
		pass

class ConcreteFlyweight(Flyweight):
	def operation(self, extrinsic_state):
		pass


def main():
	flyweight_factory = FlyweightFactory()
	concrete_flyweight = flyweight_factory.get_flyweight_key("key")
	concrete_flyweight.operation(None)

if __name__ == '__main__':
	main()