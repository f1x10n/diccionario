#prueba git03
import itertools as iter
from itertools import chain, dropwhile, repeat
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
alfab = alfabeto
#longitud mínima de la contraseña
min_lon = 3
#longitud máxima de la contraseña
max_lon = 4
#numero de repeticiones consecutivas no permitidas
max_rep = 4

def Lista_completa():
    return (''.join(candidate) for candidate in chain.from_iterable(iter.product(alfab, repeat=i) 
        for i in range(min_lon, max_lon + 1)))

lista = Lista_completa()


# for w in lista:
#     if len(w) > max_rep:
#         print("Palabra: {}. Ventanas: {}. repeticiones continuas : {}".format(w, list(miter.windowed(w, 3)),
#         list(coun(x).most_common(1)[0][1] for x in list(miter.windowed(w, 3)))
#         ))

def Ventana(palabra, largo_ventana):
    #devuelve una lista de ventanas
    return list(miter.windowed(palabra, largo_ventana))

def Chequeo_ventanas(lista_ventanas, repeticiones_maximas):
    #devuelve True si las ventanas tienen repeticiones de caracteres iguales o mayores al máximo permitido
    for v in lista_ventanas:
        if coun(v).most_common(1)[0][1] >= repeticiones_maximas:
            return True
            break

def Chequeo_palabra(palabra, repeticiones_maximas=max_rep):
    #devuelve True si la palabra tiene caracteres consecutivos mayores al maximo permitido
    return Chequeo_ventanas(Ventana(palabra, repeticiones_maximas), repeticiones_maximas)

lista_f = list(iter.filterfalse(Chequeo_palabra, lista))

# lista = Lista_completa()
# for w in lista:
#     print(w)

for w in lista_f:
    print("{} {}".format("".join(w), "Contraseña válida."))
    file.write("".join(w)+"\n")




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