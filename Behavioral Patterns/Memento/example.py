class Memento:
	def __init__(self, state):
		self.state = state

class Originator:
	def __init__(self):
		self.state = None

	def set_state(self, state):
		print("Originator: Setting state to " + str(state))
		self.state = state

	def save(self):
		print("Originator: Saving to Memento.")
		return Memento(self.state)

	def restore(self, memento):
		self.state = memento.state
		print("Originator: State after restoring from Memento. " + str(self.state))

class Caretaker:
	def __init__(self):
		self.mementos = []

	def add_memento(self, memento):
		self.mementos.append(memento)
	
	def get_memento(self):
		return self.mementos[-1]


def main():
	caretaker = Caretaker()
	originator = Originator()
	originator.set_state("State1")
	originator.set_state("State2")
	caretaker.add_memento(originator.save())
	originator.set_state("State3")
	caretaker.add_memento(originator.save())
	originator.set_state("State4")
	originator.restore(caretaker.get_memento())

if __name__ == "__main__":
    main()