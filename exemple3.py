import pulp
import numpy as np
import matplotlib.pyplot as plt

# Définition du problème
prob = pulp.LpProblem("Chargement_Cargo", pulp.LpMaximize)

x1 = pulp.LpVariable("Lots_BANANE", lowBound=0)
x2 = pulp.LpVariable("Lots_SOJA", lowBound=0)

# Fonction objectif : Max bénéfice
prob += 4.4 * x1 + 5.4 * x2

# Contraintes
prob += x1 + x2 <= 1000                  # Pétrole
prob += 0.4 * x1 + 0.2 * x2 <= 450       # Bananes
prob += 0.3 * x1 + 0.6 * x2 <= 450       # Soja

# Résolution
prob.solve()

print("=== Exemple 3 : Commerce des Lots ===")
print("Statut :", pulp.LpStatus[prob.status])
print(f"x1 (Lots BANANE) = {x1.varValue:.2f}")
print(f"x2 (Lots SOJA)   = {x2.varValue:.2f}")
print(f"Bénéfice maximal Z = {pulp.value(prob.objective):.2f} $")

# Quantités réellement chargées
petrole = x1.varValue + x2.varValue
bananes = 0.4 * x1.varValue + 0.2 * x2.varValue
soja = 0.3 * x1.varValue + 0.6 * x2.varValue

print("\n--- Quantités obtenues ---")
print(f"Pétrole : {petrole:.2f} barils")
print(f"Bananes : {bananes:.2f} tonnes")
print(f"Soja    : {soja:.2f} tonnes")

# ---- Graphique ----
x = np.linspace(0, 1200, 400)
c1 = 1000 - x
c2 = (450 - 0.4*x) / 0.2
c3 = (450 - 0.3*x) / 0.6

plt.plot(x, c1, label="Pétrole")
plt.plot(x, c2, label="Bananes")
plt.plot(x, c3, label="Soja")

plt.xlim(0, 1200)
plt.ylim(0, 1200)

plt.fill_between(x, 0, np.minimum.reduce([c1, c2, c3]), alpha=0.3, color='lightblue')
plt.scatter([x1.varValue], [x2.varValue], color='red', s=80, label="Solution optimale")

plt.xlabel("Lots BANANE (x1)")
plt.ylabel("Lots SOJA (x2)")
plt.title("Zone Faisable + Solution Optimale")
plt.legend()
plt.grid(True)
plt.show()
