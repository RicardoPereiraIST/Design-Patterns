import collections.abc
from itertools import product

class Stack(collections.abc.Iterable):
	def __init__(self):
		self.items = [None] * 10
		self.sp = -1

	def push(self, _in):
		self.sp += 1
		self.items[self.sp] = _in

	def pop(self):
		value = self.items[self.sp]
		self.sp -= 1
		return value

	def is_empty(self):
		return (self.sp == -1)

	def __iter__(self):
		return StackIterator(self)

class StackIterator(collections.abc.Iterator):
	def __init__(self, iterable):
		self.iterable = iterable
		self.index = 0

	def first(self):
		self.index = 0

	def __next__(self):
		self.index += 1

	def is_done(self):
		return (self.index == self.iterable.sp + 1)

	def current_item(self):
		return self.iterable.items[self.index]

def equals(stack_1, stack_2):
	iterator_1 = stack_1.__iter__()
	iterator_2 = stack_2.__iter__()

	iterator_1_index = iterator_1.first()
	iterator_2_index = iterator_2.first()

	while not iterator_1.is_done():
		if iterator_1.current_item() != iterator_2.current_item():
				break
		iterator_1_index = iterator_1.__next__()
		iterator_2_index = iterator_2.__next__()

	return iterator_1.is_done() and iterator_2.is_done()

def main():
	stack_1, stack_2, stack_3, stack_4, stack_5 = Stack(), Stack(), Stack(), Stack(), Stack()
	for i in range(5):
		stack_1.push(i)
		stack_2.push(i)
		stack_3.push(i)
		stack_4.push(i)
		stack_5.push(i)

	stack_3.pop()
	stack_5.pop()
	stack_4.push(2)
	stack_5.push(9)

	print("1 == 2 is " + str(equals(stack_1, stack_2)))
	print("1 == 3 is " + str(equals(stack_1, stack_3)))
	print("1 == 4 is " + str(equals(stack_1, stack_4)))
	print("1 == 5 is " + str(equals(stack_1, stack_5)))

if __name__ == "__main__":
    main()