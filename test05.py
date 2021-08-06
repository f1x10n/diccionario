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
alfa = "abcdeE"
#longitud mínima de la contraseña
min_lon = 3
#longitud máxima de la contraseña
max_lon = 4
#numero de repeticiones consecutivas no permitidas
max_rep = 4

def Lista_completa(caracteres=alfa, minimo=min_lon, maximo=max_lon):
    #crea una lista de contraseñas desde un mínimo de caracteres hasta un máximo basado en un alfabeto dado
    return (''.join(candidate) for candidate in chain.from_iterable(iter.product(caracteres, repeat=i) 
        for i in range(minimo, maximo + 1)))

lista = Lista_completa()

def Ventana(palabra, largo_ventana):
    #devuelve una lista de ventanas del largo especificado
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

for w in lista_f:
    print(w)
    file.write("".join(w)+"\n")
