def add(n1, n2):
    return n1 + n2
    
def substract(n1, n2):
    return n1 - n2
    
def multiply(n1, n2):
    return n1 * n2
    
def divide(n1, n2):
    return n1 / n2

#add these 4 functions into a dictionary. Keys

operations = {'+': add,'-': substract, '*': multiply, 'divide': divide}


def calculator(): 
    should_accumulate = True

    while should_accumulate:

        num1 = float(input("What is the first number: "))

        for symbol in operations:
            print(symbol)    
        operation_symbol = input("pick and operation: ")
        num2 = float(input("What is the next number: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input("Type 'y' to keep calculating, or type 'n' to finish operations")
        
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
            
            
calculator()