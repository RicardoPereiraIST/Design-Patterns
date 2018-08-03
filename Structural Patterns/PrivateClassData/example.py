import math

class CircleData:
	def __init__(self, radius, color, origin):
		self._radius = radius
		self._color = color
		self._origin = origin

	@property
	def radius(self):
		return self._radius

	@radius.setter
	def radius(self, value):
		self.radius = value

	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, value):
		self.color = value

	@property
	def origin(self):
		return self._origin

	@origin.setter
	def origin(self, value):
		self.origin = value

class Circle:
	def __init__(self, radius, color, origin):
		self.circleData = CircleData(radius, color, origin)

	def circumference(self):
		return self.circleData.radius * math.pi

	def diameter(self):
		return self.circleData.radius * 2

	def draw(self):
		print("Draw")


def main():
	radius, color, origin = 5, "white", (0,0,0)

	circle = Circle(radius, color, origin)
	print(circle.circumference())
	print(circle.diameter())
	circle.draw()

if __name__ == "__main__":
    main()