class Dog():
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def bark(self):
		print(self.name, "Says Bark!")
		
		
	def birthday(self):
		print(f"{self.name} is now {self.age + 1}")

dog1 = Dog("Rador", 2)
dog1.bark()
dog1.birthday()