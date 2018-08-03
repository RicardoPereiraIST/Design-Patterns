import abc

class Strategy(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def solve(self):
		pass

class StrategySolution(Strategy, metaclass=abc.ABCMeta):
	def solve(self):
		self.start()
		while self.next_try() and not self.is_solution():
			pass
		self.stop()

	@abc.abstractmethod
	def start(self):
		pass

	@abc.abstractmethod
	def next_try(self):
		pass

	@abc.abstractmethod
	def is_solution(self):
		pass

	@abc.abstractmethod
	def stop(self):
		pass

class FOO(StrategySolution):
	def __init__(self):
		self.state = 1

	def start(self):
		print("Start", end = '	', flush = True)

	def next_try(self):
		print("Next Try - " + str(self.state), end = '	', flush = True)
		self.state += 1
		return True

	def is_solution(self):
		solution = (self.state == 3)
		print("Is solution - " + str(solution), end = '	', flush = True)
		return solution

	def stop(self):
		print("Stop")

class StrategySearch(Strategy, metaclass=abc.ABCMeta):
	def solve(self):
		while True:
			self.pre_process()
			if self.search():
				break
			self.post_process()

	@abc.abstractmethod
	def pre_process(self):
		pass

	@abc.abstractmethod
	def search(self):
		pass

	@abc.abstractmethod
	def post_process(self):
		pass

class BAR(StrategySearch):
	def __init__(self):
		self.state = 1

	def pre_process(self):
		print("Pre Process", end = '	', flush = True)

	def search(self):
		print("Search - " + str(self.state), end = '	', flush = True)
		self.state += 1
		return (self.state == 3)

	def post_process(self):
		print("Post Process", end = '	', flush = True)


def main():
	algorithms = [FOO(), BAR()]
	for algorithm in algorithms:
		algorithm.solve()

if __name__ == "__main__":
    main()