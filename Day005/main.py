# scores = [1,23,25,12,2,80,9]


# max_score = 0

# for score in scores:
#     if score > max_score:
#         max_score = score


# print(max_score)


# total = 0
# for number in range(1,101):
#     total += number
# print(total)
    

# FIZZBUZZ GAME

for number in range(1,101,1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
