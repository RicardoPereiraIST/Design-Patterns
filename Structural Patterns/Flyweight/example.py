import abc

class Gazilion:
	def __init__(self, row):
		self.row = row
		print(self.row)

	def report(self, col):
		print(str(self.row) + str(col), end = ' ', flush = True)

class Factory:
	def __init__(self, max_rows):
		self.pool = [None] * max_rows

	def getFlyweight(self, row):
		if self.pool[row] == None:
			self.pool[row] = Gazilion(row)

		return self.pool[row]


def main():
	rows, cols = 6, 10
	factory = Factory(rows)

	for i in range(rows):
		for j in range(cols):
			factory.getFlyweight(i).report(j)
		print()

if __name__ == '__main__':
	main()