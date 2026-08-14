import random

word_list =  ["camello", "tigre", "leon", "ardilla", "perro", "murcielago"]

choosen_word = random.choice(word_list)

print(choosen_word)

#check if the letter guessed is one of the letters in the word, if yes print Correct, if not print wrong
placeholder = ""

for letter in choosen_word:
    placeholder += "_"

print(placeholder)

#ask the user to guess a letter and assing their answer to a variable called guess. Make guess lowercase
guess = input("Guess a letter broder: ").lower()

mod_place = []

for letter in choosen_word:
    if guess == letter:
        mod_place.append(letter)
    else:
        mod_place.append("_")


render = ''.join(mod_place)

print(render)