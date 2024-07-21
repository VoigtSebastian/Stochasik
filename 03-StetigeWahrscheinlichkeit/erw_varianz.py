#!/usr/bin/env python3
import scipy.integrate
import tabulate

# -----------------------------------------------------------------------------
# setup
# -----------------------------------------------------------------------------


# hier die Verteilungsdichtefunktion f(x) angeben NICHT F(x)
def f(x):
    return (3 / 215) * pow(x, 2)


# hier die Schranken angeben
untere_schranke = 1
obere_schranke = 6

# -----------------------------------------------------------------------------
# calc
# -----------------------------------------------------------------------------

erwartungswert = scipy.integrate.quad(
    lambda x: x * f(x), untere_schranke, obere_schranke
)[0]
varianz = scipy.integrate.quad(lambda x: x * x * f(x), untere_schranke, obere_schranke)[
    0
] - (erwartungswert**2)

# -----------------------------------------------------------------------------
# output
# -----------------------------------------------------------------------------

output = [["Erwartungswert", erwartungswert], ["Varianz", varianz]]
print(tabulate.tabulate(output, headers=["Name", "Wert"], tablefmt="fancy_grid"))
