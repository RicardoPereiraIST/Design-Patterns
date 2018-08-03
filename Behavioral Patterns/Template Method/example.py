import abc
from random import randint

class AbstractSort(metaclass=abc.ABCMeta):
	def sort(self, v):
		n = len(v)
		g = n // 2
		while g > 0:
			i = g
			while i < n:
				j = i - g
				while j >= 0:
					if self.need_swap(v[j], v[j + g]):
						v[j], v[j + g] = v[j + g], v[j]
					j -= g
				i += 1
			g //= 2

	@abc.abstractmethod
	def need_swap(self, a, b):
		pass

class SortUp(AbstractSort):
	def need_swap(self, a, b):
		return (a > b)

class SortDown(AbstractSort):
	def need_swap(self, a, b):
		return (a < b)


def main():
	NUM = 10
	array = [randint(0, 9) for i in range(NUM)]
	print(array)

	sort_objects = [SortUp(), SortDown()]
	sort_objects[0].sort(array)
	print(array)
	sort_objects[1].sort(array)
	print(array)


if __name__ == "__main__":
    main()