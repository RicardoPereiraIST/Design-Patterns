'''
Encapsulate the absence of an object by providing a substitutable
alternative that offers suitable default do nothing behavior.
'''

import abc

class AbstractObject(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def request(self):
		pass

class RealObject(AbstractObject):
	def request(self):
		pass

class NullObject(AbstractObject):
	def request(self):
		pass


def main():
	pass

if __name__ == "__main__":
    main()