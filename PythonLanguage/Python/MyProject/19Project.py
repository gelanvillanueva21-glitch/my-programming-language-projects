class Person:
	
	def __init__(self ,name , talk ):
		self.name = name
		self.talk = talk
		
	
	def Talk(self):
		print(f"{self.name} Said {self.talk}")
		
		
person = Person("Gelan", "Hello")
person.Talk()