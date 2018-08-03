'''
Provide a way to access the elements of an aggregate objects equentiallywithout exposing its underlying representation.
'''

import collections.abc

class ConcreteAggregate(collections.abc.Iterable):
	def __init__(self):
		self.data = None

	def __iter__(self):
		return ConcreteIterator(self)

class ConcreteIterator(collections.abc.Iterator):
	def __init__(self, iterable):
		self.iterable = iterable

	def __next__(self):
		if not self.has_next():
			raise StopIteration
		return None

	def has_next(self):
		pass

def main():
	for i in ConcreteAggregate():
		pass

if __name__ == "__main__":
    main()