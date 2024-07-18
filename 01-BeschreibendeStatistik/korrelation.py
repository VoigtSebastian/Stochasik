#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import tabulate

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------

a = [302, 308, 238, 203, 243, 308, 328, 297, 315, 211]
b = [62, 47, 15, 37, 53, 56, 93, 59, 57, 35]

# -----------------------------------------------------------------------------
# Output
# -----------------------------------------------------------------------------

print("Korrelationskoeffizient")
print(tabulate.tabulate(np.corrcoef(a, b), tablefmt="simple_grid"))
print()


regression_output = []
regression = stats.linregress(a, b)
regression_output.append(["Steigung", regression.slope])
regression_output.append(["Achsenabschnitt", regression.intercept])
regression_output.append(["Korrelationskoeffizient", regression.rvalue])
regression_output.append(["p-Wert", regression.pvalue])
regression_output.append(["Standardfehler", regression.stderr])

print("Regressionskoeffizient")
print(
    tabulate.tabulate(
        regression_output, headers=["Name", "Wert"], tablefmt="fancy_grid"
    )
)

# -----------------------------------------------------------------------------
# Plot
# -----------------------------------------------------------------------------

#  scatterplot
fig, ax = plt.subplots()
plt.plot(a, b, "o")
ax.set_xlabel("A")
ax.set_ylabel("B")
plt.show()
