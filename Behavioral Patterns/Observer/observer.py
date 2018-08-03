'''
Define a one-to-many dependency between objects so that when one object
changes state, all its dependents are notified and updatedautomatically.
'''

import abc

class Subject:
	def __init__(self):
		self.observers = set()
		self._subject_state = None

	def attach(self, observer):
		observer.subject = self
		self.observers.add(observer)

	def detach(self, observer):
		observer.subject = None
		self.observers.discard(observer)

	def notify(self):
		for observer in self.observers:
			observer.update(self._subject_state)

	@property
	def subject_state(self):
		return self._subject_state

	@subject_state.setter
	def subject_state(self, arg):
		self._subject_state = arg
		self.notify()

class Observer(metaclass=abc.ABCMeta):
	def __init__(self):
		self.subject = None
		self.observer_state = None

	@abc.abstractmethod
	def update(self, arg):
		pass

class ConcreteObserver(Observer):
	def update(self, arg):
		self.observer_state = arg


def main():
	subject = Subject()
	concrete_observer = ConcreteObserver()
	subject.attach(concrete_observer)
	subject.subject_state = 123
	subject.notify()
	print(str(concrete_observer.observer_state))

if __name__ == "__main__":
    main()