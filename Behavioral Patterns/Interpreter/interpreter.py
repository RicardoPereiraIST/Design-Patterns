'''
Define a represention for a grammar of the given language along with an
interpreter that uses the representation to interpret sentences in the
language.
'''

import abc

class AbstractExpression(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def interpret(self):
		pass

class TerminalExpression(AbstractExpression):
	def interpret(self):
		pass

class NonTerminalExpression(AbstractExpression):
	def __init__(self, expression):
		self.expression = expression

	def interpret(self):
		self.expression.interpret()


def main():
	abstract_syntax_tree = NonTerminalExpression(TerminalExpression())
	abstract_syntax_tree.interpret()

if __name__ == "__main__":
    main()