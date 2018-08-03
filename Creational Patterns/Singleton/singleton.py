"""
Ensure a class only has one instance, and provide a global point of
access to it.
"""

class Singleton(type):
	def __init__(cls, name, bases, attrs, **kwargs):
		super().__init__(name, bases, attrs)
		cls.instance = None

	def __call__(cls, *args, **kwargs):
		if cls.instance is None:
			cls.instance = super().__call__(*args, **kwargs)
		return cls.instance

class MyClass(metaclass = Singleton):
	pass


def main():
	m1 = MyClass()
	m2 = MyClass()
	print(m1 is m2)

if __name__ == '__main__':
	main()