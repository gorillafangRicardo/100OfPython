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

#checar si haz ganado
#checar si el dealer gana
#checar si es un empate

m_result = m_num1 + m_num2
u_result = u_num1 + u_num2

if m_result == 21:
    print("The dealer wins")
elif u_result == 21:
    print("You win!")
elif u_result == m_result:
    print("Its a draw")
elif m_result > 21:
    print(f"The dealer got {m_result} you win!")
elif u_result > 21:
    print(f"You got {u_result} you lose!")
else:
    print("I think you  got a do something about it")