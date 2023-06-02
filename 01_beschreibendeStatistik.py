#!/usr/bin/env python3

from dataclasses import dataclass
import numpy as np
from scipy import stats


list = [3, 4, 5, 1, 5, 2, 1, 3, 1, 3]
list.sort()

f = "⎸{:<50}| {:010.4f} ⎸"
[print("_", end="") for _ in range(64)]
print()
print(f.format("Minimum", np.min(list)))
print(f.format("Maximum", np.max(list)))
print(f.format("Spannweite", np.max(list) - np.min(list)))
print(f.format("Arithmetisches Mittel / Mittel / Erwartungswert", np.mean(list)))
print(f.format("25%-Quantil", np.quantile(list, 0.25)))
print(f.format("30%-Quantil", np.quantile(list, 0.3)))
print(f.format("66%-Quantil", np.quantile(list, 0.66)))
print(f.format("Varianz", np.var(list, ddof=1)))
print(f.format("Standardabweichung", np.std(list, ddof=1)))
print(
    f.format("Interquartilabstand", np.quantile(list, 0.75) - np.quantile(list, 0.25))
)
# TODO: Median
[print("‾", end="") for _ in range(64)]
print()
