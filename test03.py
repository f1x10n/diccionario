#prueba git02
import itertools as iter
from itertools import chain
import more_itertools as miter
from collections import Counter as coun
import cardinality as card

alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
minusculas = alfabeto[0:26]
mayusculas = alfabeto[26:52]
numeros = alfabeto[52:]

#crea archivo .txt
file = open("wordlist.txt", "w+")

#caracteres usados para crear lista de contraseñs
alfab = alfabeto
#longitud mínima de la contraseña
min_lon = 3
#longitud máxima de la contraseña
max_lon = 4
#numero de repeticiones consecutivas no permitidas
max_rep = 2

#Crea un iterador con resultado tuples de longitud igual a "repeat" usando los caracteres de la cadena entregada
# lista = ""
# for i in range(min_lon, max_lon + 1):
#     lista = iter.chainn(for w in iter.product(alfab, repeat=i))

# lista = iter.product(alfab, repeat=1)

def Lista():
    return chain.from_iterable(iter.product(alfab, repeat=i)
        for i in range(min_lon, max_lon + 1))

lista = Lista()

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