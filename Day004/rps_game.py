import random

rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''



player_pick = int(input("Lets play rock, paper, scissors! \n Type 0 for rock, 1 for paper or 2 for scissors "))
machine_pick = random.randint(0,2)

print(f"computer chose {machine_pick}")

if player_pick == 0 and machine_pick == 2:
    print("you won!")
elif machine_pick == 2 and player_pick == 0:
    print("you lost!")
elif machine_pick > player_pick:
    print("you lost")
elif player_pick > machine_pick:
    print("you won!")
elif player_pick == machine_pick:
    print("its a draw")

