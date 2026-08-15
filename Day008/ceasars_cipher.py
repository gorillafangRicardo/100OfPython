# name = input("whats your name")

# def greet(name):
#     print(f"hello {name}")
#     print("felisidadess")
#     print("tontorron")



# greet(name)

#calcular mis semanas de vida

#restar las semanas de vida con las que tendria si tuviera 90 y/o
# final_age = 4680


# def life_in_weeks(age):
#     converter = age * 52
#     final_result = final_age - converter
#     print(f"You have {final_result} weeks left.")


# life_in_weeks(20)


#functions with more than 1 input

# def greet_with(name, location):
#     print(f"Hello {name} from {location}")


# greet_with( location="Saltillo",name="Ricardo")
true_word = "true"
love_word = "love"




def calculate_love_score(name1, name2):
    first_number = 0
    second_number = 0
    merge_names = name1 + name2

    for letter in merge_names:
        if letter in true_word:
            first_number += 1

    for letter in merge_names:
        if letter in love_word:
            second_number += 1


    love_result = str(first_number) + str(second_number)
    print(love_result)



calculate_love_score("Kanye West", "Kim Kardashian")

