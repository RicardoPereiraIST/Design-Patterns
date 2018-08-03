import abc

class AbstractFactory(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def create_curved_instance(self):
		pass

	@abc.abstractmethod
	def create_straight_instance(self):
		pass

class SimpleShapeFactory(AbstractFactory):
	def create_curved_instance(self):
		return Circle()

	def create_straight_instance(self):
		return Square()

class RobustShapeFactory(AbstractFactory):
	def create_curved_instance(self):
		return Elipse()

	def create_straight_instance(self):
		return Rectangle()

class Shape(metaclass=abc.ABCMeta):
	_total = 0

	def __init__(self):
		Shape._total += 1
		self._id = Shape._total

	@abc.abstractmethod
	def draw(self):
		pass

class Circle(Shape):
	def draw(self):
		print("Cirle " + str(self._id) + ": draw")

class Square(Shape):
	def draw(self):
		print("Square " + str(self._id) + ": draw")

class Elipse(Shape):
	def draw(self):
		print("Elipse " + str(self._id) + ": draw")

class Rectangle(Shape):
	def draw(self):
		print("Rectangle " + str(self._id) + ": draw")

class Client:
	def __init__(self, concrete_factory):
		self.factory = concrete_factory()


def main():
	for client in (Client(SimpleShapeFactory), Client(RobustShapeFactory)):
		curved_shape = client.factory.create_curved_instance()
		straight_shape = client.factory.create_straight_instance()

		curved_shape.draw()
		straight_shape.draw()

if __name__ == '__main__':
	main()