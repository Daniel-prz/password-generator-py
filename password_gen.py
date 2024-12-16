import random
letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','q',"r","s","t","u","v","w","x","y","z"]
symbol_list = ['!','#','%','&','*','(',')','=','+']
number_list = ['1','2','3','4','5','6','7','8','9']

nr_letters = int(input("How many letters wanted in password?\n"))
nr_numbers = int(input("How many numbers wanted in password?\n"))
nr_symbols = int(input('How many symbols wanted in password?\n'))

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letter_list))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(number_list))

for char in range(1,nr_symbols + 1):
    password_list.append(random.choice(symbol_list))

(random.shuffle(password_list))

password = ''

for char in password_list:
    password += char

print(f'password generated: {password}')