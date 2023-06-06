#!/usr/bin/env python3

from dataclasses import dataclass
import math
import numpy as np
from scipy import stats

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------

list = [2, 4, 3, 1, 2, 4, 2, 2, 2, 3]
quantile = [0.25, 0.3, 0.66]

list.sort()


def print_separator(sep="_"):
    [print(sep, end="") for _ in range(64)]
    print()


def print_quantile(v, q):
    print(f.format(f"{int(v*100)}-Quantil", q))


# -----------------------------------------------------------------------------
# Output
# -----------------------------------------------------------------------------

f = "⎸{:<50}| {:010.4f} ⎸"
print_separator()
print(f.format("Minimum", np.min(list)))
print(f.format("Maximum", np.max(list)))
print(f.format("Spannweite", np.max(list) - np.min(list)))
print_separator(sep="-")
print(f.format("Arithmetisches Mittel / Mittel / Erwartungswert", np.mean(list)))
print(f.format("Varianz", np.var(list, ddof=1)))
print(f.format("Standardabweichung", np.std(list, ddof=1)))
print(f.format("Median", np.median(list)))

print_separator(sep="-")

for quant in quantile:
    quantil = len(list) * quant
    if quantil.is_integer():
        q = np.quantile(list, quant, method="midpoint")
        print_quantile(quant, q)
    else:
        q = list[math.ceil(quant * len(list)) - 1]
        print_quantile(quant, q)


print_separator(sep="‾")


# -----------------------------------------------------------------------------
# Plotting
# -----------------------------------------------------------------------------
