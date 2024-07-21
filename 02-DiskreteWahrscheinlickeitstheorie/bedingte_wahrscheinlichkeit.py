#! /usr/bin/env python3
from icecream import ic

#
# wenn disjunkt
#
# A vereinigt   B = A∪B = P(A) + P(B)
#
# wenn unabhängig:
#
# A geschnitten B = A∩B = P(A) * P(B) (wenn unabhängig)
#                 --> nur Schnittmenge in Mitte A/B
# A vereinigt   B = A∪B = P(A) + P(B) - P(A∩B) (wenn unabgängig)
#                 --> gesamtes Bild (A A/B B)
#
# P(A∪B) = P(A) + P(B) - P(A∩B)
# P(A∩B) = P(A) + P(B) - P(A∪B)
# __________________________________________
# B unter der Bedindung A = P(B|A)
#
# P(B|A)  =   P(A∩B)
#             ________
#             P(A)
#
# Satz der totalen Wahrscheinlichkeit:
# P(A)    =   P(B)*(A|B) + P(~B) * P(A|~B)
#
# P(A∩B)  =   P(A)*P(B|A)
#         =   P(B)*P(A|B)
#
# Bayes:
# P(B|A)  =   P(B)*P(A|B)
#             __________
#             P(A)
# __________________________________________
# Beispiel:
P_A = 0.345
P_B = 0.3
P_A_bedB = 0.055
P_B_bedA = P_B * P_A_bedB / P_A
ic(P_B_bedA)

# Beispiel:
# BürgermeisterWahl: Alice(A) und Bob(B)
# Bezirke: Wahlbezirk Links (L) und Rechts (R)
#
# 60% der Wähler kommen aus R, 40 % aus L
# Alice erhält aus R 30%
# Bob erhält aus L 80%
#
# P(L) = 40%
# P(A|L) = 80%
# P(B|L) = 20%
#
# P(R) = 60%
# P(A|R) = 30%
# P(B|R) = 70%
#
# P(A)    = P(L)*P(A|L) + P(R)*P(A|R)
#         = 0.4 * 0.8 + 0.6 * 0.3
#         = 50 %
# from icecream import ic
# P_A = 0.6
# P_B = 0.5
# P_A_u_B = 0.9 # P(A) oder P(B) oder P(A ∩ B)
#
# # BEIDE
# P_A_n_B = P_A + P_B - P_A_u_B
# ic(P_A_n_B)
#
# # KEINES
# P_nichtA_n_nichtB = 1 - P_A_u_B
# ic(P_nichtA_n_nichtB)
#
# # EINES ABER NICHT BEIDE
# ic(P_A_u_B - P_A_n_B)
#

#
