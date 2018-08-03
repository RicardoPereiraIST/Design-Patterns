import abc

class AlarmListener(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def alarm(self):
		pass

class SensorSystem:
	def __init__(self):
		self.listeners = []

	def register(self, listener):
		self.listeners.append(listener)

	def sound_the_alarm(self):
		for listener in self.listeners:
			listener.alarm()

class Lightning(AlarmListener):
	def alarm(self):
		print("Lights up.")

class Gates(AlarmListener):
	def alarm(self):
		print("Gates close.")

class Checklist:
	def by_the_numbers(self):
		self.localize()
		self.isolate()
		self.identify()

	def localize(self):
		print("	Establish a perimeter.")

	def isolate(self):
		print("	Isolate the grid.")

	def identify(self):
		print("	Identify the source.")

class Surveillance(Checklist, AlarmListener):
	def alarm(self):
		print("Surveillance - by the numbers:")
		self.by_the_numbers()

	def isolate(self):
		print("	Train the cameras.")


def main():
	sensor_system = SensorSystem()
	sensor_system.register(Gates())
	sensor_system.register(Lightning())
	sensor_system.register(Surveillance())
	sensor_system.sound_the_alarm()

if __name__ == "__main__":
    main()