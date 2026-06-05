
Balance = 0

def Check_Balance(Balance):
	print()
	print("Your balance: ", Balance)
	

def Deposit(Balance):
	print()
	print("Deposit Amount")
	
	try:
		amount = int(input("> "))
		Balance += amount
		return Balance
	except ValueError:
		print("Invalid Input!")
	
	
def Withdraw(Balance):
	print("Withdraw Amount")
	
	try:
		if Balance == 0:
			print("You can't Withdraw")
			return
		else:
			print()
			
		withdraw = int(input("> "))
		
		if Balance - withdraw < 0:
			print("Insufficient Balance")
		else:
			Balance -= withdraw
			print("Successfully Withdraw")
			print("Amount: ", withdraw)
			return Balance
	
	except ValueError:
		print("Invalid Input")
	
def Main(Balance):
	print("-------ATM-------")
	
	try:
		while True:
			print("""

1. Check Balance
2. Deposit
3. Withdraw
4. Exit
	
	""")
	
			choose = int(input("> "))
			
			if choose == 1:
				Check_Balance(Balance)
			elif choose == 2:
				Balance = Deposit(Balance)
			elif choose == 3:
				Balance = Withdraw(Balance)
			elif choose == 4:
				return
		
	except ValueError:
		print("Invalid Input!")
	

Main(Balance)