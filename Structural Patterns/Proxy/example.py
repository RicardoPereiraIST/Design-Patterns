import abc

class Person:
	next = 0
	person_list = ["Tom", "Dick", "Harry", "Bubba"]

	def __init__(self):
		self.name = Person.person_list[self.next]
		Person.next += 1

class PettyCashProtected:
	def __init__(self):
		self.balance = 500

	def withdraw(self, amount):
		if amount > self.balance:
			return False

		self.balance -= amount
		return True

class PettyCash:
	real_thing = PettyCashProtected()

	def withdraw(self, person, amount):
		if person.name == "Tom" or person.name == "Harry" or person.name == "Bubba":
			return PettyCash.real_thing.withdraw(amount)
		return False


def main():
	petty_cash = PettyCash()
	workers = [Person(), Person(), Person(), Person()]

	amount = 100
	for i in range(4):
		if not petty_cash.withdraw(workers[i], amount):
			print("No money for " + workers[i].name)
		else:
			print(str(amount) + " dollars for " + workers[i].name)
		amount += 100
	print("Remaining balance is " + str(petty_cash.real_thing.balance))



if __name__ == "__main__":
    main()