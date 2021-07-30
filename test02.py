import itertools as iter
import more_itertools as miter
from collections import Counter as coun
import cardinality as card

import argparse, sys, threading, time
from datetime import datetime
from itertools import chain, product
from ftplib import FTP

alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
minusculas = alfabeto[0:26]
mayusculas = alfabeto[26:52]
numeros = alfabeto[52:]

def bruteforce(charset, maxlength, minlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(minlength, maxlength + 1)))


wl = bruteforce("abcde", 4, 3)
for i in wl:
    print(i)