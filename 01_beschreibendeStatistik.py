#!/usr/bin/env python3

import matplotlib.pyplot as plt
import math
import numpy as np
import tabulate

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------

values = [25, 10, 30, 25, 35, 25]
quantile = [0.75]
counts = {}

output = []

values.sort()


def add_quantile(v, q):
    output.append([f"{int(v*100)}-Quantil", q])


def modalwert(list):
    for i in list:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return max(counts, key=counts.get)


# -----------------------------------------------------------------------------
# Output
# -----------------------------------------------------------------------------

output.append(["Minimum", np.min(values)])
output.append(["Maximum", np.max(values)])
output.append(["Spannweite", np.max(values) - np.min(values)])
output.append(["Arithmetisches Mittel / Erwartungswert", np.mean(values)])
output.append(["Median", np.median(values)])
output.append(["Varianz", np.var(values, ddof=1)])
output.append(["Standardabweichung", np.std(values, ddof=1)])
output.append(["Modalwert", modalwert(values)])


for quant in quantile:
    quantil = len(values) * quant
    if quantil.is_integer():
        q = np.quantile(values, quant, method="midpoint")
        add_quantile(quant, q)
    else:
        q = values[math.ceil(quant * len(values)) - 1]
        add_quantile(quant, q)

print(tabulate.tabulate(output, headers=["Name", "Wert"], tablefmt="fancy_grid"))

# -----------------------------------------------------------------------------
# Plotting
# -----------------------------------------------------------------------------

plt.bar(list(counts.keys()), list(counts.values()), edgecolor="black", linewidth=1.2)
plt.show()
