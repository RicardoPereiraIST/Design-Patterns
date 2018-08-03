import abc

class Chain:
	def __init__(self):
		self.current_state = Off()

	def pull(self):
		self.current_state.pull(self)

class State(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def pull(self, wrapper):
		wrapper.current_state = Off()
		print("	Turning off.")

class Off(State):
	def pull(self, wrapper):
		wrapper.current_state = Low()
		print("	Low speed.")

class Low(State):
	def pull(self, wrapper):
		wrapper.current_state = Medium()
		print("	Medium speed.")

class Medium(State):
	def pull(self, wrapper):
		wrapper.current_state = High()
		print("	High speed.")

class High(State):
	def pull(self, wrapper):
		State.pull(self, wrapper)


def main():
	chain = Chain()
	while True:
		_input = str(input("Press Enter "))
		if _input != '':
			break
		chain.pull()

if __name__ == "__main__":
    main()