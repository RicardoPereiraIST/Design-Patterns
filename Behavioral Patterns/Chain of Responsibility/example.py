import abc
from random import randint

class Image(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def process(self):
		pass

class IR(Image):
	def process(self):
		return "IR"

class LS(Image):
	def process(self):
		return "LS"

class Processor:
	next_id = 1

	def __init__(self):
		self.id = Processor.next_id
		Processor.next_id += 1

	def execute(self, img):
		if randint(0,1) != 0:
			print("	Processor " + str(self.id) + " is busy")
			return False

		print("Processor " + str(self.id) + " - " + img.process())
		return True


def main():
	input_images = [IR(), IR(), LS(), IR(), LS(), LS()]
	processors = [Processor(), Processor(), Processor()]
	images_size = len(input_images)
	processors_size = len(processors)

	for i in range(images_size):
		print("Operation #" + str(i + 1) + ":")
		j = 0
		while not processors[j].execute(input_images[i]):
			j = (j + 1) % processors_size
		print()

if __name__ == "__main__":
    main()