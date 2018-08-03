'''
Encapsulate a request as an object, thereby letting you parameterize
clients with different requests, queue or log requests, and support
undoable operations.
'''

import abc

class Invoker:
	def __init__(self):
		self.commands = []

	def store_command(self, command):
		self.commands.append(command)

	def execute_commands(self):
		for command in self.commands:
			command.execute()

class Command(metaclass=abc.ABCMeta):
	def __init__(self, receiver):
		self.receiver = receiver

	@abc.abstractmethod
	def execute(self):
		pass

class ConcreteCommand(Command):
	def execute(self):
		self.receiver.action()

class Receiver:
	def action(self):
		pass


def main():
	receiver = Receiver()
	concrete_command = ConcreteCommand(receiver)
	invoker = Invoker()
	invoker.store_command(concrete_command)
	invoker.execute_commands()

if __name__ == "__main__":
    main()