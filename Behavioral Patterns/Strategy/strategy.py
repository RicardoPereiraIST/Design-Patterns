'''
Define a family of algorithms, encapsulate each one, and make them
interchangeable. Strategy lets the algorithm vary independently from
clients that use it.
'''

import abc

class Context:
	def __init__(self, strategy):
		self.strategy = strategy

	def context_interface(self):
		self.strategy.algorithm_interface()

class Strategy(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def algorithm_interface(self):
		pass

class ConcreteStrategyA(Strategy):
	def algorithm_interface(self):
		pass

class ConcreteStrategyB(Strategy):
	def algorithm_interface(self):
		pass


def main():
	concrete_strategy_a = ConcreteStrategyA()
	context = Context(concrete_strategy_a)
	context.context_interface()

if __name__ == "__main__":
    main()