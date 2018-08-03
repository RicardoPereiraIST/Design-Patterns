'''
Provide a surrogate or placeholder for another object to control access
to it or add other responsibilities.
'''

import abc

class Subject(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def request(self):
		pass

class Proxy(Subject):
	def __init__(self, real_subject):
		self.real_subject = real_subject

	def request(self):
		self.real_subject.request()

class RealSubject(Subject):
	def request(self):
		pass


def main():
	proxy = Proxy(RealSubject())
	proxy.request()


if __name__ == "__main__":
    main()