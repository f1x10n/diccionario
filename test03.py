#prueba git03
import itertools as iter
from itertools import chain, repeat
import more_itertools as miter
from collections import Counter as coun
import cardinality as card

alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
minusculas = alfabeto[0:26]
mayusculas = alfabeto[26:52]
numeros = alfabeto[52:]

#crea archivo .txt
file = open("wordlist.txt", "w+")

#caracteres usados para crear lista de contraseñas
# alfab = alfabeto
alfab = "abc"
#longitud mínima de la contraseña
min_lon = 2
#longitud máxima de la contraseña
max_lon = 3
#numero de repeticiones consecutivas no permitidas
max_rep = 3

def Lista_rep():
    if max_rep >= 2:
        return chain.from_iterable(iter.product(w, repeat=i) 
            for w in alfab for i in range(1, max_rep))

alfa_rep = Lista_rep()


def Permutaciones():
    return chain.from_iterable(iter.permutations(alfa_rep, i) for i in range(min_lon, max_lon + 1))

lista = Permutaciones()

def flatten(list_of_lists):
    "Flatten one level of nesting"
    return chain.from_iterable(list_of_lists)

lista = map(flatten, lista)

for w in lista:
    print(w)

#filtra el iterador cuando 
# lista_filtrada = iter.filterfalse(lambda x: coun(x).most_common(1)[0][1] >= max_rep, lista_bruta)

# lista_filtrada = iter.filterfalse(lambda x: , lista_bruta)

# for word in lista_filtrada:
#     print(word)



# #por cada contraseña en la lista
# for con in lista:
#     #carácter repetido demasiadas veces consecutivas
#     car_rep = ""
#     #mientras la contraseña sea valida
#     contraseña_valida = True
#     while contraseña_valida == True:
#         #por cada caracter en la contraseña
#         for car in range(max_lon - max_rep + 1):
#             # print("{} {}".format(con[car], con.count(con[car])))
#             #si el caracter esta repetido en la contraseña igual o mayor al maximo de repeticiones consecutivas permitidas
#             if con.count(con[car]) >= max_rep:
#                 repeticiones = 1
#                 #cuenta el numero de repeticiones consecutivas del caracter
#                 for n in range(max_rep - 1):
#                     if con[car + n] == con[car + n + 1]:
#                         repeticiones += 1
#                 #si las repeticiones consecutivas son iguales o mayor a lo permitido entonces la contraseña es invalida
#                 if repeticiones >= max_rep:
#                     contraseña_valida = False
#                     car_rep = con[car]
#         break
#     if contraseña_valida == True:
#         print("{} {}".format("".join(con), "Contraseña válida."))
#         file.write("".join(con)+"\n")
#     else:
#         print("{} {} {} {}".format("".join(con), "Contraseña inválida. El caracter", car_rep, "repetido demasiadas veces consecutivas."))