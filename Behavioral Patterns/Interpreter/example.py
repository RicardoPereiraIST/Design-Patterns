import abc

class RNInterpreter:
	def __init__(self):
		self.thousands = Thousand(1)
		self.hundreds = Hundred(1);
		self.tens = Ten(1);
		self.ones = One(1);

	def interpret(self, _input):
		total = [0]
		self.thousands.parse(_input, total)
		self.hundreds.parse(_input, total)
		self.tens.parse(_input, total)
		self.ones.parse(_input, total)

		if _input != [""]:
			return 0
		return total[0]

	def parse(self, _input, total):
		index = 0

		if _input[0][:2] == self.nine():
			total[0] += 9 * self.multiplier()
			index += 2
		elif _input[0][:2] == self.four():
			total[0] += 4 * self.multiplier()
			index += 2
		else:
			if _input[0][0] == self.five():
				total[0] += 5 * self.multiplier()
				index = 1
			else:
				index = 0

			end = index + 3
			if end > len(_input[0]):
				end = len(_input[0])

			while index < end:
				if _input[0][index] == self.one():
					total[0] += 1 * self.multiplier()
				else:
					break
				index += 1

		_input[0] = _input[0][index::]

	@abc.abstractmethod
	def one(self):
		pass

	@abc.abstractmethod
	def four(self):
		pass

	@abc.abstractmethod
	def five(self):
		pass

	@abc.abstractmethod
	def nine(self):
		pass

	@abc.abstractmethod
	def multiplier(self):
		pass

class Thousand(RNInterpreter):
	def __init__(self, value):
		pass

	def one(self):
		return 'M'

	def four(self):
		return ""

	def five(self):
		return '\0'

	def nine(self):
		return ""

	def multiplier(self):
		return 1000

class Hundred(RNInterpreter):
	def __init__(self, value):
		pass

	def one(self):
		return 'C'

	def four(self):
		return "CD"

	def five(self):
		return 'D'

	def nine(self):
		return "CM"

	def multiplier(self):
		return 100

class Ten(RNInterpreter):
	def __init__(self, value):
		pass

	def one(self):
		return 'X'

	def four(self):
		return "XL"

	def five(self):
		return 'L'

	def nine(self):
		return "XC"

	def multiplier(self):
		return 10

class One(RNInterpreter):
	def __init__(self, value):
		pass

	def one(self):
		return 'I'

	def four(self):
		return "IV"

	def five(self):
		return 'V'

	def nine(self):
		return "IX"

	def multiplier(self):
		return 1


def main():
	interpreter = RNInterpreter()
	print("Enter Roman Numeral:")
	value = [input()]
	while value != ['']:
		print("	Interpretation is: " + str(interpreter.interpret(value)))
		print("Enter Roman Numeral:")
		value = [input()]

if __name__ == "__main__":
    main()