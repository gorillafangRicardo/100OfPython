code_dic = {"bug": "cosas malas que pasan", "function": "funciones o codigo repetido"}

# print(code_dic["bug"])

code_dic["loop"] = "una cosa que se repite"

print(code_dic)


for thing in code_dic:
    print(thing)
    print(code_dic[thing])
