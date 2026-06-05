print("start - to start the car")
print("stop - to stop the car")
print("quit - to exit")

Car_Started = False

while True:
	pick = str(input(">")).upper()
	
	if pick == "START":
		if Car_Started:
			print("Car Already Started!")
		else:
			Car_Started = True
			print("Car Started... ready to go!")
	elif pick == "STOP":
		if not Car_Started:
			print("Car Already Stopped")
		else:
			Car_Started = False
			print("Car Stopped")
	elif pick == "QUIT":
		break
	elif pick != "START" and pick != "STOP" and pick != "QUIT":
		print("Sorry I Can't Understand")
	
	