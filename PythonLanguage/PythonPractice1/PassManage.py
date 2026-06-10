
class Account:
    def __init__(self):
        self.account_info = {}


    def menu(self):
        while True:
            print("\n1. Account\n2. View Account\n3. Exit")

            try:
                choose = int(input("> "))

                if choose == 1:
                    social = input("Social Media: ")
                    username = input("Create Username: ")
                    if len(username) >= 8:
                        password = input("Create Password: ")
                        if len(password) >= 8:
                            print('Successfuly Created Account')
                            self.account_info[social] = {"Username": username, "Password": password}
                    else:
                        print("Must be 8 characters")
                elif choose == 2:
                    for value, info in self.account_info.items():
                        print(value, info)
                elif choose == 3:
                    break
                else:
                    print('Wrong Input')
            
            except ValueError:
                print("Enter A NUMBER!!")
                continue


acc = Account()
acc.menu()