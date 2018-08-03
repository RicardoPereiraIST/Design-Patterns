import abc

class Document(metaclass=abc.ABCMeta):
	def __init__(self, name):
		self.name = name

	@abc.abstractmethod
	def open(self):
		pass

	@abc.abstractmethod
	def close(self):
		pass

class MyDocument(Document):
	def open(self):
		print("	MyDocument: open()")

	def close(self):
		print("	MyDocument: close()")

class Application:
	def __init__(self):
		self.index = 0
		self.docs = [None] * 10
		print("Application")

	def new_document(self, name):
		print("Application: new_document()")
		
		if self.index > 9:
			print("Can't create more documents")
			return

		self.docs[self.index] = self.create_document(name)
		self.docs[self.index].open()
		self.index += 1

	@abc.abstractmethod
	def create_document(self, name):
		pass

	def report_docs(self):
		print("Application: report_docs()")
		for i in range(self.index):
			print("	" + self.docs[i].name)

class MyApplication(Application):
	def __init__(self):
		Application.__init__(self)
		print("MyApplication")

	def create_document(self, name):
		print("	MyApplication: create_document()")
		return MyDocument(name)
		

def main():
	my_app = MyApplication()
	my_app.new_document("foo")
	my_app.new_document("bar")
	my_app.report_docs()

if __name__ == '__main__':
	main()