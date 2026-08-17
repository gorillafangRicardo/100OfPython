alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(r'''  ______     ___       _______     _______.     ___      .______           ______  __  .______    __    __   _______ .______      
 /      |   /   \     |   ____|   /       |    /   \     |   _  \         /      ||  | |   _  \  |  |  |  | |   ____||   _  \     
|  ,----'  /  ^  \    |  |__     |   (----`   /  ^  \    |  |_)  |       |  ,----'|  | |  |_)  | |  |__|  | |  |__   |  |_)  |    
|  |      /  /_\  \   |   __|     \   \      /  /_\  \   |      /        |  |     |  | |   ___/  |   __   | |   __|  |      /     
|  `----./  _____  \  |  |____.----)   |    /  _____  \  |  |\  \----.   |  `----.|  | |  |      |  |  |  | |  |____ |  |\  \----.
 \______/__/     \__\ |_______|_______/    /__/     \__\ | _| `._____|    \______||__| | _|      |__|  |__| |_______|| _| `._____|
                                                                                                                                  ''')
def main():

    to_do = input("Write 'ENCODE' or 'DECODE': ").lower()
    message = input("Write your message: ").lower()
    shift = int(input("Tell me the secret number: "))



    def decrypt(text = message, shift = shift):

        full_mess = []

        for letter in text:
            if letter in alphabet:
                index = alphabet.index(letter)

                encrypted = (index - shift) % len(alphabet)   
                full_mess.append(alphabet[encrypted])

            else:
                full_mess.append(letter)

        resultado = "".join(full_mess)

        print(f"Here is your decrypted message: {resultado}")
        restart = input("would you like to restart?: ").lower()


        if restart == 'y':
            main()
        else:
            return




    def encrypt(text = message, shift = shift):

        full_mess = []

        for letter in text:
            if letter in alphabet:
                index = alphabet.index(letter)

                encrypted = (index + shift) % len(alphabet)
                full_mess.append(alphabet[encrypted])

            else:
                full_mess.append(letter)

        resultado = "".join(full_mess)

        print(f"Here is your encrypted message: {resultado}")
        restart = input("would you like to restart?: ").lower()


        if restart == 'y':
            main()
        else:
            return


    def caesar():
        if to_do == "encode":
            encrypt(text = message, shift = shift)
        else:
            decrypt(text = message, shift = shift)


    caesar()


main()