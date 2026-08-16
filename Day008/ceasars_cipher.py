alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']

to_do = input("Write 'ENCODE' or 'DECODE").lower
message = input("Write your messagge")
shift = int(input("Tell me the secret number"))


#puedo sacar el index de cada letra y sumarle el shift number para encriptar el mensaje
def encrypt():

    full_mess = []
    
    for letter in message:
        encrypted = alphabet.index(letter) + shift
        full_mess.append(alphabet[encrypted])
    
        
    resultado = "".join(full_mess)        
    print(resultado)
    

encrypt()


 