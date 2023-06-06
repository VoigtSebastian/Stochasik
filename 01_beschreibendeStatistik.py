#!/usr/bin/env python3

import matplotlib.pyplot as plt
import math
import numpy as np
import tabulate

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------

list = [25, 10, 30, 25, 35, 25]
quantile = [0.75]
output = []

list.sort()


def add_quantile(v, q):
    output.append([f"{int(v*100)}-Quantil", q])


def modalwert(list):
    counts = {}
    for i in list:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return max(counts, key=counts.get)


# -----------------------------------------------------------------------------
# Output
# -----------------------------------------------------------------------------

output.append(["Minimum", np.min(list)])
output.append(["Maximum", np.max(list)])
output.append(["Spannweite", np.max(list) - np.min(list)])
output.append(["Arithmetisches Mittel / Erwartungswert", np.mean(list)])
output.append(["Median", np.median(list)])
output.append(["Varianz", np.var(list, ddof=1)])
output.append(["Standardabweichung", np.std(list, ddof=1)])
output.append(["Modalwert", modalwert(list)])


for quant in quantile:
    quantil = len(list) * quant
    if quantil.is_integer():
        q = np.quantile(list, quant, method="midpoint")
        add_quantile(quant, q)
    else:
        q = list[math.ceil(quant * len(list)) - 1]
        add_quantile(quant, q)

print(tabulate.tabulate(output, headers=["Name", "Wert"], tablefmt="fancy_grid"))

# -----------------------------------------------------------------------------
# Plotting
# -----------------------------------------------------------------------------

plt.hist(list, len(set(list)), edgecolor="black", linewidth=1.2)
plt.title("Histogramm")
plt.show()
