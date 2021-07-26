import itertools as iter

alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
minusculas = alfabeto[0:26]
mayusculas = alfabeto[26:52]
numeros = alfabeto[52:]

print(minusculas)
print(mayusculas)
print(numeros)

# lista = iter.product("abc", repeat=3)

# file = open("wl.titet,", "w+")

# for ite in lista:
#     print("{} {} {} {} {}".format(ite, ",len =", len(ite), ", type =", type(ite)))
#     print(ite)

    # print(type(ite))
    # for nchar in range(len(ite)):
    #     if ite[nchar] == ite[nchar+1] and ite[nchar+1] == ite[nchar+2]:
    #         print(ite)

res = iter.product('abc', repeat=3) # 3 is the length of your result.
for i in res: 
    print(''.join(i))