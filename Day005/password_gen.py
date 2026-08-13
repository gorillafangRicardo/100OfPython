import random

letters = ['a','b','c','d','e','h','i','j','k','l','m','n','o']
numbers = [1,2,3,4,5,6,7,8,9,0]
symbols = ['!','@','#','$','%','^','&','*','(',')']

#ask number of letters
nr_letters = int(input("Tell me how many letters"))
#ask number of numbers
nr_numbers = int(input("Tell me how many numbers"))
# #number of symbols
nr_symbols = int(input("Tell me how many symbols"))

password = ""

for letter in range(1, nr_letters + 1):
    password += random.choice(letters)
for number in range(1, nr_numbers + 1):
    password += str(random.choice(numbers))
for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)


listed = list(password)
random.shuffle(listed)
shuffled = ''.join(listed)

print(shuffled)