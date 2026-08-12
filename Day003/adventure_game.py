print('''         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|''')

print("Welcome to the treasure island.\nYour mission is to find the tresure")
path = input("Choose a path to go Left or Right? ").lower()


if path == "left":
    print("Well done! You can go the next phase")

    path = input("There is a river!\n What do you want to do? Swim or Wait?" ).lower()

    if path == "wait":
        print("I can see you are patient")

        path = input("3 Magic doors appear infront of you!\n What door will you take? Red, Blue or Yellow?").lower()

        if path == "yellow":
            print("You win mafarkerrrr")
        else:
            print("This is a game over for you pal hehe")

    else:
        print("You drowned mafarkerrr Game Over")

else:
    print("Game Over broski")


