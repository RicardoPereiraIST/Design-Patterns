'''
Provide a unified interface to a set of interfaces in a subsystem.
Facade defines a higher-level interface that makes the subsystem easier
to use.
'''

from os.path import dirname, abspath
import imp

#Facade should be a Singleton
parent_folder = dirname(dirname(dirname(abspath(__file__))))
singleton = imp.load_source('Singleton', parent_folder+'\\Creational Patterns\\Singleton\\singleton.py')


#Singleton Class
class Facade(metaclass = singleton.Singleton):
	def __init__(self):
		self.sub_system_1 = SubSystem1()
		self.sub_system_2 = SubSystem2()

	def operation(self):
		self.sub_system_1.operation_1()
		self.sub_system_1.operation_2()
		self.sub_system_2.operation_1()
		self.sub_system_2.operation_2()

class SubSystem1:
	def operation_1(self):
		pass

	def operation_2(self):
		pass

class SubSystem2:
	def operation_1(self):
		pass

	def operation_2(self):
		pass


def main():
	facade = Facade()
	facade.operation()


if __name__ == '__main__':
	main()