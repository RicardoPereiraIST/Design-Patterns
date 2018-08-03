import abc

class AbstractStream(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def write(self, b):
		pass

class NullOutputStream(AbstractStream):
	def write(self, b):
		pass

class NullPrintStream(AbstractStream):
	def __init__(self):
		self.stream = NullOutputStream()

	def write(self, b):
		self.stream.write(b)

class Application:
	def __init__(self, debug_out):
		self.debug_out = debug_out

	def do_something(self):
		s = 0
		for i in range(10):
			s += i
			self.debug_out.write("i = " + str(i))

		print("sum = " + str(s))


def main():
	app = Application(NullPrintStream())
	app.do_something()

if __name__ == "__main__":
    main()