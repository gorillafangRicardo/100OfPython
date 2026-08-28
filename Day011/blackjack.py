import random

win = False
#imprimir dos numero random de esa lista y que sean del usuario

#imprimir generar dos numeros random de esa lista y solo imprimir uno

#crear un deck de cartas
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

m_num1 = random.choice(deck)
m_num2 = random.choice(deck)

u_num1 = random.choice(deck)
u_num2 = random.choice(deck)

#imprimir generar dos numeros random de esa lista y solo imprimir uno
print(f"This is the dealers card: {m_num1}")

#imprimir dos numero random de esa lista y que sean del usuario
print(f"These are your cards: {u_num1} {u_num2}")


#checar si haz ganado
#checar si el dealer gana
#checar si es un empate

m_result = m_num1 + m_num2
u_result = u_num1 + u_num2

#hacer que haya opcion de pedir otra carta
#sumar esa carta a lo que ya tienes

choice = input("Hit card or stand?: ").lower()


while not win:        
    if m_result == 21:
        print("The dealer wins")
        win == True
    elif u_result == 21:
        print("You win!")
        win == True
    elif u_result == m_result:
        print("Its a draw")
        win == True
    elif m_result > 21:
        print(f"The dealer got {m_result} you win!")
        win == True
    elif u_result > 21:
        print(f"You got {u_result} you lose!")
        win == True
    else:
        print("I think you  got a do something about it")
        print(f"the dealers cards were: {m_num1} and {m_num2}")
        win == True

    if choice == "hit":
        u_result += random.choice(deck)
        print(m_result)
    else:
        print("You stand")
