import random

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



m_result = m_num1 + m_num2
u_result = u_num1 + u_num2

#hacer que haya opcion de pedir otra carta
#sumar esa carta a lo que ya tienes

def check_result():

    end_game = False

    while end_game == False:
        if u_result == 21:
            print(f"Player win with {u_result}")
            end_game = True
        elif m_result == 21:
            print(f"Player lose against the machine!")
            end_game = True
        elif m_result > u_result and m_result < 21:
            print(f"The machine wins!!")
            end_game = True



stand = False


while stand == False:

    choice = input("Hit card or stand?: ").lower()

    if choice == "hit":
        u_result = u_result + random.choice(deck)
        print(u_result)
        if u_result > 21:
            print("You lost!")
            break            
    else:
        print(f"You stand with {u_result}")
        check_result()
        stand = True

