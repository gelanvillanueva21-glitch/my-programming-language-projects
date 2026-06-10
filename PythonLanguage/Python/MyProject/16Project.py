Key = False
Stop = True

def Look_Around():
	while True:
		print("")
		print("1. Cabinet")
		print("2. Comfort Room")
		print("3. Vault")
		print("4. Get Back")
		choose = int(input("> "))
		
		if choose == 1:
			print("No Key")
		elif choose == 2:
			print("No Key")
		elif choose == 3:
			print("Can't Access")
		elif choose == 4:
			return
		else:
			print("Wrong Choice")
		print("")



def Open_Door(Key, Stop):
	print("")
	if Key:
		print("You've Escaped!!")
		return False
	else:
		print("The Door Is Locked")
		return True
	print("")
	
		


def Check_Inventory(Key):
	print("")
	if Key:
		print("You already had the Key")
		return Key
	else:
		print("You found the key!")
		return True
	print("")


def Main(Key, Stop):
	
	while Stop:
		print("1. Look Around")
		print("2. Open The Door")
		print("3. Check Inventory")
		print("4. Quit")
		
		choice = int(input("> "))
		
		if choice == 1:
			Look_Around()
		elif choice == 2:
			Stop = Open_Door(Key, Stop)
		elif choice == 3:
			Key = Check_Inventory(Key)
		elif choice == 4:
			break


print("You are in a dark room.")
Main(Key, Stop)