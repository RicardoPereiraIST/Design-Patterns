from os.path import dirname, abspath
import imp

#ObjectPool should be a Singleton
parent_folder = dirname(dirname(abspath(__file__)))
singleton = imp.load_source('Singleton', parent_folder+'\\Singleton\\singleton.py')

#Singleton Class
class ObjectPool(metaclass = singleton.Singleton):
	def __init__(self):
		self.resources = []

	def get_resource(self):
		if not self.resources:
			print("Creating new.")
			return Resource()
		else:
			print("Reusing existing")
			return self.resources.pop()

	def return_resource(self, resource):
		resource.reset()
		self.resources.append(resource)

class Resource:
	def __init__(self):
		self.value = 0

	def reset(self):
		self.value = 0

	def set_value(self, value):
		self.value = value

def main():
	pool = ObjectPool()

	resource_one = pool.get_resource()
	resource_two = pool.get_resource()
	resource_one.set_value(10)
	resource_two.set_value(20)
	print(resource_one.value, resource_two.value)

	pool.return_resource(resource_one)
	pool.return_resource(resource_two)
	resource_one = pool.get_resource()
	resource_two = pool.get_resource()
	print(resource_one.value, resource_two.value)


if __name__ == '__main__':
	main()