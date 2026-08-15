import random
import hangman_words

hangman = [r'''  +---+
  O   |
 /|\  |
 / \  |
     ===
''',r'''  +---+
  O   |
 /|\  |
 /    |
     ===
''',r'''  +---+
  O   |
 /|\  |
      |
     ===
''',r'''  +---+
  O   |
 /|   |
      |
     ===
''',r'''  +---+
  O   |

  |   |
      |
     ===
''',r'''  +---+
      |
      |
      |
     ===
''']


choosen_word = random.choice(hangman_words.word_list)

print(choosen_word)

#check if the letter guessed is one of the letters in the word, if yes print Correct, if not print wrong
placeholder = ""

for letter in choosen_word:
    placeholder += "_"

print(placeholder)

#ask the user to guess a letter and assing their answer to a variable called guess. Make guess lowercase

you_win = False

#crear una funcion que hace un overwrite a el placeholder con las letras correctas

correct_letters = []  

total_lives = 6


while not you_win:


    mod_place = []


    guess = input("Guess a letter broder: ").lower()

    

    for letter in choosen_word:
        if guess == letter:
            mod_place.append(letter)
            correct_letters.append(guess)

        elif letter in correct_letters:
            mod_place += letter
       
        else:
            mod_place.append("_")

            
    if guess not in choosen_word:
        total_lives -= 1
        print(hangman[total_lives])
        print(f"{guess} IS NOT IN WORD!")
        
    if guess in mod_place:
        print(f"YOU ALREADY GUESSED {guess}")



    render = ''.join(mod_place)

    print(render)



    if not "_" in mod_place:
        you_win = True
        print("you win")
    elif total_lives == 0:
        you_win = False
        print("You lose!")
        print(f"The word was '{choosen_word}'")
        break