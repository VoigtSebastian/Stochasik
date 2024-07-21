#!/usr/bin/env python3

import matplotlib.pyplot as plt
import math
import numpy as np
import tabulate

# -----------------------------------------------------------------------------
# setup
# -----------------------------------------------------------------------------

# input values
values = [25, 17, 25, 29, 20, 15, 11, 17, 16, 16]
quantile = [0.10, 0.25, 0.5, 0.75, 0.9]

# output values
counts = {}
output = []
values.sort()


def add_quantile(v, q):
    output.append([f"{int(v*100)}-Quantil", q, f"x̃̃_{v}"])


def calc_quantile(quant):
    quantil = len(values) * quant
    if quantil.is_integer():
        return np.quantile(values, quant, method="midpoint")
    return values[math.ceil(quant * len(values)) - 1]


def modalwert(list):
    for i in list:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return max(counts, key=counts.get)


# -----------------------------------------------------------------------------
# output
# -----------------------------------------------------------------------------

output.append(["Minimum", np.min(values), "min"])
output.append(["Maximum", np.max(values), "max"])
output.append(["Spannweite", np.max(values) - np.min(values), "R"])
output.append(
    [
        "Arithmetisches Mittel / Erwartungswert / Mittelwert",
        np.mean(values),
        "̅̅x (typische Anzahl)",
    ]
)
output.append(["Median", np.median(values), "x̃̃"])
output.append(["Varianz", np.var(values, ddof=1), "s^2"])
# Die Standardabweichung der Stichprobe
output.append(["Standardabweichung (gefragt)", np.std(values, ddof=1), "s"])
# Die Standardabweichung der Population - normalerweise nicht gefragt
output.append(["Standardabweichung Population", np.std(values, ddof=0), "σ"])
output.append(["Modalwert", modalwert(values), "x_mod"])


for quant in quantile:
    quantil = calc_quantile(quant)
    add_quantile(quant, quantil)


output.append(
    ["Interquartilabstand", calc_quantile(0.75) - calc_quantile(0.25), "I(-QR)"]
)

print(
    tabulate.tabulate(
        output, headers=["Name", "Wert", "Zeichen"], tablefmt="fancy_grid"
    )
)

# -----------------------------------------------------------------------------
# plotting
# -----------------------------------------------------------------------------

if False:
    plt.bar(
        list(counts.keys()), list(counts.values()), edgecolor="black", linewidth=1.2
    )
    plt.show()
