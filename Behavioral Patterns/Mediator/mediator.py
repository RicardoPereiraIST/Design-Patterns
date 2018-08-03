'''
Define an object that encapsulates how a set of objects interact.
Mediator promotes loose coupling by keeping objects from referring to
each other explicitly, and it lets you vary their interaction
'''

class Mediator:
	def __init__(self):
		self.colleague_1 = Colleague1(self)
		self.colleague_2 = Colleague2(self)

class Colleague:
	def __init__(self, mediator):
		self.mediator = mediator

class Colleague1(Colleague):
	pass

class Colleague2(Colleague):
	pass

def main():
	mediator = Mediator()

if __name__ == "__main__":
    main()