'''
Convert the interface of a class into another interface clients expect.
Adapter lets classes work together that couldn't otherwise because of
incompatible interfaces.
'''

import abc

class Target(metaclass=abc.ABCMeta):
	def __init__(self):
		self.adaptee = Adaptee()

	@abc.abstractmethod
	def request(self):
		pass

class Adapter(Target):
	def request(self):
		self.adaptee.specific_request()

class Adaptee:
	def specific_request(self):
		pass


def main():
	adapter = Adapter()
	adapter.request()

if __name__ == '__main__':
	main()