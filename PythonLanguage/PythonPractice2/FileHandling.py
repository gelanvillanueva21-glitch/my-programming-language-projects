try:
    with open("Dino.txt", 'x') as file:
        file.write('Hello')

except FileExistsError:
    print("File Already Exist!")
except FileNotFoundError:
    print(f"Failed To Find File: {file}")
else:
    print("Code Succesfuly, Execute")