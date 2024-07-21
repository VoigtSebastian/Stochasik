#!/usr/bin/env python3
from scipy import special
from tabulate import tabulate

n = 36
k = 5

table = [
    # Binomialkoeffizient: Anzahl der Möglichkeiten aus einer Menge mit n Elementen, eine Teilmenge mit k Elementen auszuwählen
    # z.B. 36 Zeichen Passwortliste, 5 Zeichen Passwort
    ["Binomialkoeffizient", special.binom(n, k)],
    # 0. Permutation (Alle und ohne Wiederholung)
    ["Permutation (Alle und ohne Wiederholung)", special.factorial(n, exact=True)],
    # 1. Variation (Geordnete Auswahl)
    # 1.1 ohne Wiederholungen
    ["Variation (ohne Wiederholung)", special.perm(n, k, exact=True)],
    # 1.2 mit Wiederholungen
    # z.B. PIN 4-stellig aus Ziffern 0-9
    ["Variation (mit Wiederholung)", pow(n, k)],
    # Kombination (Ungeordnete Auswahl)
    # 1.1 ohne Wiederholungen,
    # z.B. 2 Socken aus Schublade von 8 Socken ziehen
    # hier dran denken: Häufig in Aufgaben Gegenereignis hilft!
    [
        "Kombination (ohne Wiederholung)",
        special.comb(n, k, repetition=False, exact=True),
    ],
    # 1.2 mit Wiederholungen,
    ["Kombination (mit Wiederholung)", special.comb(n, k, repetition=True, exact=True)],
    ["Factorial", special.factorial(k, exact=True)],
]

headers = ["Type", "Result"]
table_str = tabulate(table, headers, tablefmt="fancy_grid")
print(table_str)
