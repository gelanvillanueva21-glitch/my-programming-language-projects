
def main():
    file = open('Notes.txt', 'a+')

    while True:
        print("1. Write A New Notes\n2. View Notes\n3. Exit")

        try:
            choose = int(input("> "))

            if choose == 1:
                print("Write Something New")
                words = input("> ")
                file.write(words + "\n")
            elif choose == 2:
                file.seek(0)
                print(file.read())
            elif choose == 3:
                break
            else:
                print(f"Number {choose} is not in a List")
        except ValueError:
            print('Wrong Input!!')
        except FileNotFoundError:
            print('File Not Found')

    file.close()

main()