
import math

class PointCartesian:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def move(self, x, y):
		self.x += x
		self.y += y

	def to_string(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"

class PointPolar:
	def __init__(self, radius, angle):
		self.radius = radius
		self.angle = angle

	def rotate(self, angle):
		self.angle += angle % 360

	def to_string(self):
		return "[" + str(self.radius) + "@" + str(self.angle) + "]"

class Point:
	def __init__(self, x, y):
		self.point_cartesian = PointCartesian(x,y)

	def to_string(self):
		return self.point_cartesian.to_string()

	def move(self, x, y):
		self.point_cartesian.move(x, y)

	def rotate(self, angle, point):
		x = self.point_cartesian.x - point.point_cartesian.x
		y = self.point_cartesian.y - point.point_cartesian.y
		point_polar = PointPolar(math.sqrt(x * x + y * y), math.atan2(y, x) * 180 / math.pi)
		point_polar.rotate(angle)
		print("	PointPolar is " + point_polar.to_string())
		string = point_polar.to_string()[1:-1]
		partition = string.split('@')
		r, a = float(partition[0]), float(partition[1])
		self.point_cartesian = PointCartesian(r * math.cos(a * math.pi / 180) + point.point_cartesian.x, r * math.sin(a * math.pi / 180) + point.point_cartesian.y)

class Line:
	def __init__(self, origin, end):
		self.origin = origin
		self.end = end

	def move(self, x, y):
		self.origin.move(x, y)
		self.end.move(x, y)

	def rotate(self, angle):
		self.end.rotate(angle, self.origin)

	def to_string(self):
		return "origin is " + self.origin.to_string() + ", end is " + self.end.to_string()


def main():
	line_a = Line(Point(2,4), Point(5,7))
	line_a.move(-2, -4)
	print("after move: " + line_a.to_string())
	line_a.rotate(45)
	print("after rotate: " + line_a.to_string())
	line_b = Line(Point(2,1), Point(2.866, 1.5))
	line_b.rotate(30)
	print("30 degrees to 60 degrees: " + line_b.to_string())	


if __name__ == '__main__':
	main()