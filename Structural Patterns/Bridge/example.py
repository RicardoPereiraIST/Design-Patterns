import abc
from random import randint

class Stack:
	def __init__(self, stack):
		self.implementor = stack

	def push(self, n):
		self.implementor.push(n)

	def pop(self):
		return self.implementor.pop()

	def is_empty(self):
		return self.implementor.empty()

class StackHanoi(Stack):
	def __init__(self, stack):
		Stack.__init__(self, stack)
		self.total_rejected = 0

	def push(self, n):
		if not Stack.is_empty(self) and n > self.implementor.peek():
			self.total_rejected += 1
		else:
			Stack.push(self, n)

class StackImp(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def push(self, o):
		pass

	def peek(self):
		if self.total > -1:
			return self.items[self.total]

	def empty(self):
		return self.total == -1

	@abc.abstractmethod
	def pop(self):
		pass

class StackJava(StackImp):
	def __init__(self):
		self.items = []
		self.total = -1

	def push(self, o):
		self.total += 1
		self.items.append(o)
		self.peek()

	def pop(self):
		o = self.peek()
		self.items = self.items[:-1]
		self.total -= 1
		return o

class StackMine(StackImp):
	def __init__(self):
		self.items = [None] * 20
		self.total = -1

	def push(self, o):
		if not self.total < 19:
			print("Stack is full.")
		else:
			self.total += 1
			self.items[self.total] = o
			self.peek()

	def pop(self):
		o = self.peek()
		self.total -= 1
		return o


def main():
	stacks = [Stack(StackJava()), Stack(StackMine()), StackHanoi(StackJava()), StackHanoi(StackMine())]
	size = len(stacks)

	for i in range(20):
		num = randint(0, 39)
		for stack in stacks:
			stack.push(num)

	for i in range(size):
		while not stacks[i].is_empty():
			print(str(stacks[i].pop()), end = "	", flush = True)
		print()
	print("Total rejected is " + str(stacks[3].total_rejected))

if __name__ == '__main__':
	main()