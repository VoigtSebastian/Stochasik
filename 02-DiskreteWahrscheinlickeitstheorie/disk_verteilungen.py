#!/usr/bin/env python3
from scipy import stats
import tabulate

# 1 ----- Bernoulli Verteilung ---------
# --------------------------------------
#
#           Wurf einer Münze
#           Verschicken von 50 Datenpaketen
#
#           p = Wahrscheinlichkeit, dass etwas eintritt
#           X ~ Ber(p)

if False:
    p = 0.7
    x = 0
    print("BERNOULLI")
    output = [
        [f"P(X = {x})", stats.bernoulli(p).pmf(x)],
        [f"P(X <= {x})", stats.bernoulli(p).cdf(x)],
        [f"P(X > {x})", 1 - stats.bernoulli(p).cdf(x)],
        ["E(X)", stats.bernoulli(p).expect()],
        ["Var(X)", stats.bernoulli(p).var()],
    ]
    print(tabulate.tabulate(output, headers=["Name", "Value"], tablefmt="fancy_grid"))


# 2 ----- Gemoetrische Verteilung ------
# --------------------------------------
#
#           Anzahl der Versuche bis zum 1. Erfolg
#           Lebensdauer eines Bauteils
#
#           p = Wahrscheinlichkeit, dass etwas eintritt
#           X ~ geom(p)
if True:
    p = 0.15
    x = 20
    print("GEOMETRISCH")
    output = [
        [f"P(X = {x})", stats.geom(p).pmf(x)],
        [f"P(X <= {x})", stats.geom(p).cdf(x)],
        [f"P(X > {x})", 1 - stats.geom(p).cdf(x)],
        [f"P(X < {x}", stats.geom(p).cdf(x) - stats.geom(p).pmf(x)],
        ["Quantil", stats.geom(p).ppf(0.9)],
        ["E(X)", stats.geom(p).expect()],
        ["Var(X)", stats.geom(p).var()],
    ]
    print(tabulate.tabulate(output, headers=["Name", "Value"], tablefmt="fancy_grid"))


# 3 ----- Binomialverteilung -----------
# --------------------------------------
#
#           Anzahl an erfolgreichen Versuchen
#           Anzahl an kaputten Bauteilen / Würfe mit Augenzahl 1
#
#           n = Anzahl an Versuchen
#           p = Wahrscheinlichkeit, dass Erfolg
#           X ~ Bin(n, p)
if True:
    n = 20
    p = 0.15

    x = [20]
    quantil = 0.99
    print("BINOMIAL")
    output = [
        [f"P(X = {x})", stats.binom(n, p).pmf(x)],
        [f"P(X <= {x})", stats.binom(n, p).cdf(x)],
        [f"P(X > {x})", 1 - stats.binom(n, p).cdf(x)],
        [f"P(X < {x})", stats.binom(n, p).cdf(x) - stats.binom(n, p).pmf(x)],
        [f"P(X >= {x})", stats.binom(n, p).pmf(x) + 1 - stats.binom(n, p).cdf(x)],
        ["Quantil", stats.binom(n, p).ppf(0.9)],
        ["Erwartungswert bei Stichprobe", n * p],
        ["E(X)", stats.binom(n, p).expect()],
        ["Var(X)", stats.binom(n, p).var()],
        [f"{quantil}-Quantil", stats.binom(n, p).ppf(quantil)],
    ]
    print(tabulate.tabulate(output, headers=["Name", "Value"], tablefmt="fancy_grid"))

# 4 ----- Hypergeometrische Verteilung -
# --------------------------------------
#
#           Anzahl an Elementen mit best. Eigenschaft aus Stichprobe
#           Ziehen ohne Zurücklegen
#
#           N_g = Grundgesamtheit
#           M = Anzahl an Elementen mit Eigenschaft aus Gesamtheit
#           n = Anzahl Stichprobe
#           X ~ (N, M, n)
if True:
    N = 120
    M = 20
    n = 10

    x = 0
    print("HYPERGEOMETRISCH")
    output = [
        [f"P(X = {x})", stats.hypergeom(N, M, n).pmf(x)],
        [f"P(X <= {x})", stats.hypergeom(N, M, n).cdf(x)],
        [f"P(X > {x})", 1 - stats.hypergeom(N, M, n).cdf(x)],
        ["E(X)", stats.hypergeom(N, M, n).expect()],
        ["Var(X)", stats.hypergeom(N, M, n).var()],
    ]
    print(tabulate.tabulate(output, headers=["Name", "Value"], tablefmt="fancy_grid"))

# 5 ----- Poisson Verteilung -----------
# --------------------------------------
#
#           Anzahl der Vorkommnisse in einem best. Intervall
#
#           λ = Auftrittsrate (z.B. 3 pro Woche)
#           X ~ Po(λ)
#
#           TODO: Wie rechnet man Rate aus wenn Exp() gegeben?
if True:
    l = 3.5
    x = 1
    print("POISSON")
    output = [
        [f"P(X = {x})", stats.poisson(l).pmf(x)],
        [f"P(X <= {x})", stats.poisson(l).cdf(x)],
        [f"P(X > {x})", 1 - stats.poisson(l).cdf(x)],
        [f"P(X < {x})", stats.poisson(l).cdf(x) - stats.poisson(l).pmf(x)],
        ["Quantil", stats.poisson(l).ppf(0.9)],
        ["E(X)", stats.poisson(l).expect()],
        ["Var(X)", stats.poisson(l).var()],
    ]
    print(tabulate.tabulate(output, headers=["Name", "Value"], tablefmt="fancy_grid"))
