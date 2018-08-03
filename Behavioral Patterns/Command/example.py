import abc

class Command(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def execute(self):
		pass

class DomesticEngineer(Command):
	def execute(self):
		print("Take out the trash.")

class Politician(Command):
	def execute(self):
		print("Take money from the rich, take votes from the poor.")

class Programmer(Command):
	def execute(self):
		print("Sell the bugs, charge extra for the fixes.")

class Invoker:
	def __init__(self):
		self.commands = []

	def store_command(self, command):
		self.commands.append(command)

	def execute_commands(self):
		for command in self.commands:
			command.execute()

def main():
	invoker = Invoker()
	invoker.store_command(DomesticEngineer())
	invoker.store_command(Politician())
	invoker.store_command(Programmer())
	invoker.execute_commands()

if __name__ == "__main__":
    main()