'''
Attach additional responsibilities to an object dynamically. Decorators
provide a flexible alternative to subclassing for extending
functionality.
'''

import abc

class Widget(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def draw(self):
		pass

class TextField(Widget):
	def __init__(self, w, h):
		self.width = w
		self.height = h

	def draw(self):
		print("TextField: " + str(self.width) + ", " + str(self.height))

class Decorator(Widget, metaclass=abc.ABCMeta):
	def __init__(self, widget):
		self.widget = widget

	def draw(self):
		self.widget.draw()

class BorderDecorator(Decorator):
	def draw(self):
		Decorator.draw(self)
		print("	BorderDecorator")

class ScrollDecorator(Decorator):
	def draw(self):
		Decorator.draw(self)
		print("	ScrollDecorator")


def main():
	widget = BorderDecorator(BorderDecorator(ScrollDecorator(TextField(80, 24))))
	widget.draw()


if __name__ == '__main__':
	main()