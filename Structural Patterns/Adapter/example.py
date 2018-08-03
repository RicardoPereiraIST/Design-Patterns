import abc

class Rectangle(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def draw(self):
		pass

class LegacyRectangle:
	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		print("LegacyRectangle: create. (" + str(self.x1) + "," + str(self.y1) + ") => (" + str(self.x2) + "," + str(self.y2) + ")")

	def old_draw(self):
		print("LegacyRectangle: old_draw. (" + str(self.x1) + "," + str(self.y1) + ") => (" + str(self.x2) + "," + str(self.y2) + ")")

class RectangleAdapter(Rectangle, LegacyRectangle):
	def __init__(self, x, y, w, h):
		LegacyRectangle.__init__(self, x, y, x + w, y + h)
		print("RectangleAdapter: create. (" + str(self.x1) + "," + str(self.y1) + "), width = " + str(w) + ", height = " + str(h))

	def draw(self):
		print("RectangleAdapter: draw.")
		self.old_draw()


def main():
	rectangle = RectangleAdapter(120, 200, 60, 40)
	rectangle.draw()

if __name__ == '__main__':
	main()