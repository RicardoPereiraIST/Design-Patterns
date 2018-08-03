'''
Allow an object to alter its behavior when its internal state changes.
The object will appear to change its class.
'''

import abc

class Context:
	def __init__(self, state):
		self.state = state

	def request(self):
		self.state.handle()

class State(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def handle(self):
		pass

class ConcreteStateA(State):
	def handle(self):
		pass

class ConcreteStateB(State):
	def handle(self):
		pass


def main():
	concrete_state_a = ConcreteStateA()
	context = Context(concrete_state_a)
	context.request()

if __name__ == "__main__":
    main()