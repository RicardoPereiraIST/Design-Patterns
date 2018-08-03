'''
Capture and externalize an object's internal state so that the object
can be restored to this state later, without violating encapsulation.
'''

import pickle

class Originator:
	def __init__(self):
		self.state = None

	def create_memento(self):
		return pickle.dumps(vars(self))

	def set_memento(self, memento):
		previous_state = pickle.loads(memento)
		vars(self).clear()
		vars(self).update(previous_state)


def main():
	originator = Originator()
	memento = originator.create_memento()
	originator.state = True
	print(originator.state)
	originator.set_memento(memento)
	print(originator.state)

if __name__ == "__main__":
    main()