def turn_right():
    turn_left()
    turn_left()
    turn_left()

def salto():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear() == True:
        move()
    turn_left()
      
while not at_goal():
    if front_is_clear() == True:
        move()
    else:
        salto()
