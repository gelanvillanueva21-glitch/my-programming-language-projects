#If you use the global keyword, the variable belongs to the global scope:
	
def myfunc():
	global x
	x = "easy"
	

myfunc()

print('python is ' + x)

#Create a variable inside a function, with the same name as the global variable

y = "awesome"

def myfun():
  y = "fantastic"
  print("Python is " + y)

myfun()

print("Python is " + y)

#change the value of a global variable inside a function, refer to the variable by using the global keyword

z = "damn"

def hello():
	global z
	z = "hi"
	
hello()

print(z)