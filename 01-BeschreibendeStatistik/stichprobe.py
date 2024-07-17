#!/usr/bin/env python3

import matplotlib.pyplot as plt
import math
import numpy as np
import tabulate

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------

values = [2, 4, 3, 1, 2, 4, 2, 2, 2, 3]
quantile = [0.10, 0.25, 0.75]
counts = {}

output = []

values.sort()


def add_quantile(v, q):
    output.append([f"{int(v*100)}-Quantil", q, f"x̃̃_{v}"])


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

output.append(["Minimum", np.min(values), "min"])
output.append(["Maximum", np.max(values), "max"])
output.append(["Spannweite", np.max(values) - np.min(values), "IQR"])
output.append(["Arithmetisches Mittel / Erwartungswert", np.mean(values), "̅̅x"])
output.append(["Median", np.median(values), "x̃̃"])
output.append(["Varianz", np.var(values, ddof=1), "s^2"])
output.append(["Standardabweichung", np.std(values, ddof=1), "s"])
output.append(["Modalwert", modalwert(values), "x_mod"])


for quant in quantile:
    quantil = len(values) * quant
    if quantil.is_integer():
        q = np.quantile(values, quant, method="midpoint")
        add_quantile(quant, q)
    else:
        q = values[math.ceil(quant * len(values)) - 1]
        add_quantile(quant, q)

output.append(
    [
        "Interquartilabstand",
        np.quantile(values, 0.75, interpolation="midpoint")
        - np.quantile(values, 0.25, interpolation="midpoint"),
        "R",
    ]
)

print(
    tabulate.tabulate(
        output, headers=["Name", "Wert", "Zeichen"], tablefmt="fancy_grid"
    )
)

# -----------------------------------------------------------------------------
# Plotting
# -----------------------------------------------------------------------------

plt.bar(list(counts.keys()), list(counts.values()), edgecolor="black", linewidth=1.2)
plt.show()
