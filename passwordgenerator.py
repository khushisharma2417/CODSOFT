import random
print("This is a password generator:")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']


Letters = int(input("How many letters do you want in your password? "))
Numbers = int(input("How many numbers do you want in your password? "))
Symbols = int(input("How many symbols do you want in your password?"))

password = ""

for i in range(1,Letters+1):
    var = random.choice(letters)
    password = password+var


for i in range(1,Numbers+1):
    var = random.choice(numbers)
    password=password+var

for i in range(1,Symbols+1):
    var = random.choice(symbols)
    password=password+var



print(password)