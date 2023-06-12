#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import tabulate

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------

a = [8, 7, 5, 10, 6, 3, 9, 7]
b = [55, 60, 40, 70, 45, 40, 65, 55]

# -----------------------------------------------------------------------------
# Output
# -----------------------------------------------------------------------------

print("Korrelationskoeffizient")
print(tabulate.tabulate(np.corrcoef(a, b), tablefmt="fancy_grid"))
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
