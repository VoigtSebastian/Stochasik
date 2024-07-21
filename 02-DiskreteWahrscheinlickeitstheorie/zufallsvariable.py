#!/usr/bin/env python3

import matplotlib.pyplot as plt
import tabulate

# -----------------------------------------------------------------------------
# setup
# -----------------------------------------------------------------------------

# X = Zufallsvariable
X = [1, 2, 3]
# P_X = Wahrscheinlichkeiten der Zufallsvariable X
P_X = [2 / 6, 2 / 6, 2 / 6]

# -----------------------------------------------------------------------------
# calc
# -----------------------------------------------------------------------------

E_X = sum([X[i] * P_X[i] for i in range(len(X))])
Var_X = sum([((X[i] - E_X) ** 2) * P_X[i] for i in range(len(X))])

# -----------------------------------------------------------------------------
# cli output
# -----------------------------------------------------------------------------
output = []

output.append([f"Erwartungswert", E_X])
output.append([f"Varianz", Var_X])
output.append([f"Standardabweichung", Var_X**0.5])

print(tabulate.tabulate(output, headers=["Name", "Wert"], tablefmt="fancy_grid"))

# -----------------------------------------------------------------------------
# plot
# -----------------------------------------------------------------------------

# Bar chart
fig, ax = plt.subplots()
ax.bar(X, P_X)
ax.set_xlabel("X")
ax.set_ylabel("P(X)")
plt.show()

# Accumulated distribution function
fig, ax = plt.subplots()
ax.step(X, [sum(P_X[: i + 1]) for i in range(len(X))])
ax.set_xlabel("X")
ax.set_ylabel("F(X)")
plt.show()
