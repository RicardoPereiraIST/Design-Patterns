'''
Offer a significant performance boost; it is most effective in
situations where the cost of initializing a class instance is high, the
rate of instantiation of a class is high, and the number of
instantiations in use at any one time is low.
'''

class ReusablePool:
	def __init__(self, size):
		self.reusables = [Reusable() for _ in range(size)]

	def acquire(self):
		return self.reusables.pop()

	def release(self, reusable):
		self.reusables.append(reusable)

class Reusable:
	pass

def main():
	reusable_pool = ReusablePool(10)
	reusable = reusable_pool.acquire()
	reusable_pool.release(reusable)

if __name__ == '__main__':
	main()