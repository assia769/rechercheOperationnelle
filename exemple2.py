import pulp
import numpy as np
import matplotlib.pyplot as plt

# Données de demande
E = 125 * 10**4
G = 135 * 10**4
F = 180 * 10**4

# Définition du problème
prob = pulp.LpProblem("Raffinerie", pulp.LpMinimize)

# Variables
x1 = pulp.LpVariable("Brut_1", lowBound=0)
x2 = pulp.LpVariable("Brut_2", lowBound=0)

# Fonction objectif : Min coût
prob += 700 * x1 + 500 * x2

# Contraintes de production
prob += 0.30 * x1 + 0.25 * x2 >= E
prob += 0.40 * x1 + 0.25 * x2 >= G
prob += 0.30 * x1 + 0.50 * x2 >= F

# Résolution
prob.solve()

print("=== Raffinerie - Résultat Optimal ===")
print("Statut :", pulp.LpStatus[prob.status])
print(f"Quantité de Brut 1 (x1) = {x1.varValue:.2f} tonnes")
print(f"Quantité de Brut 2 (x2) = {x2.varValue:.2f} tonnes")
print(f"Coût minimal = {pulp.value(prob.objective):.2f} UM")

# ---- Graphique ----
x = np.linspace(0, max(x1.varValue, x2.varValue) * 2, 300)

c1 = (E - 0.30*x) / 0.25
c2 = (G - 0.40*x) / 0.25
c3 = (F - 0.30*x) / 0.50

plt.plot(x, c1, label="Essence")
plt.plot(x, c2, label="Gazole")
plt.plot(x, c3, label="Fioul")

plt.xlim(0, max(x))
plt.ylim(0, max(c1.max(), c2.max(), c3.max()))

plt.fill_between(x, np.maximum.reduce([c1, c2, c3]), color="lightblue", alpha=0.3)
plt.scatter([x1.varValue], [x2.varValue], color="red", s=80, label="Solution optimale")

plt.xlabel("Brut 1 (x1)")
plt.ylabel("Brut 2 (x2)")
plt.title("Zone Faisable - Raffinerie")
plt.legend()
plt.grid(True)
plt.show()
