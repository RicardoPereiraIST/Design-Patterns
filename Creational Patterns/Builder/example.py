import abc

class Pizza:
	def __init__(self):
		self.dough = ""
		self.sauce = ""
		self.topping = ""

	def set_dough(self, dough):
		self.dough = dough

	def set_sauce(self, sauce):
		self.sauce = sauce

	def set_topping(self, topping):
		self.topping = topping

	def get_pizza(self):
		return "Pizza made with " + self.dough + " dough, " + self.sauce + " sauce, and " + self.topping + "."

class PizzaBuilder(metaclass=abc.ABCMeta):
	def __init__(self):
		self.pizza = None

	def create_new_pizza(self):
		self.pizza = Pizza()

	def get_pizza(self):
		return self.pizza.get_pizza()

	@abc.abstractmethod
	def build_dough(self):
		pass

	@abc.abstractmethod
	def build_sauce(self):
		pass
	
	@abc.abstractmethod
	def build_topping(self):
		pass

class HawaiianPizzaBuilder(PizzaBuilder):
	def build_dough(self):
		self.pizza.set_dough("cross")

	def build_sauce(self):
		self.pizza.set_sauce("mild")
	
	def build_topping(self):
		self.pizza.set_topping("pineapple")

class SpicyPizzaBuilder(PizzaBuilder):
	def build_dough(self):
		self.pizza.set_dough("pan baked")

	def build_sauce(self):
		self.pizza.set_sauce("hot")
	
	def build_topping(self):
		self.pizza.set_topping("pepperoni")

class Waiter:
	def __init__(self):
		self.pizza_builder = None

	def get_pizza(self):
		return self.pizza_builder.get_pizza()

	def construct_pizza(self, pizza_builder):
		self.pizza_builder = pizza_builder
		self.pizza_builder.create_new_pizza()
		self.pizza_builder.build_dough()
		self.pizza_builder.build_sauce()
		self.pizza_builder.build_topping()

def main():
	waiter = Waiter()
	for pizza_builder in (HawaiianPizzaBuilder(), SpicyPizzaBuilder()):
		waiter.construct_pizza(pizza_builder)
		print(waiter.get_pizza())

if __name__ == '__main__':
	main()