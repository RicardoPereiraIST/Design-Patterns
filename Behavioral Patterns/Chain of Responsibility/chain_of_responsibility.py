'''
Avoid coupling the sender of a request to its receiver by giving
more than one object a chance to handle the request. Chain the receiving
objects and pass the request along the chain until an object handles it.
'''

import abc

class Handler(metaclass=abc.ABCMeta):
	def __init__(self, successor = None):
		self.successor = successor
		self.can_handle = True

	@abc.abstractmethod
	def handle_request(self):
		pass

class ConcreteHandler1(Handler):
	def __init__(self, successor):
		Handler.__init__(self, successor)
		self.can_handle = False

	def handle_request(self):
		if self.can_handle:
			pass
		elif self.successor != None:
			self.successor.handle_request()

class ConcreteHandler2(Handler):
	def handle_request(self):
		if self.can_handle:
			pass
		elif self.successor != None:
			self.successor.handle_request()


def main():
	handler = ConcreteHandler1(ConcreteHandler2())
	handler.handle_request()

if __name__ == "__main__":
    main()