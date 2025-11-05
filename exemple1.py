import pulp
import matplotlib.pyplot as plt
import numpy as np

# Définir le problème
prob = pulp.LpProblem("Chassis_Production", pulp.LpMaximize)

x1 = pulp.LpVariable("x1", lowBound=0)  # produit alu
x2 = pulp.LpVariable("x2", lowBound=0)  # produit bois

# Fonction objectif : Max Z = 3x1 + 5x2
prob += 3 * x1 + 5 * x2

# Contraintes
prob += x1 <= 4
prob += x2 <= 6
prob += 3 * x1 + 2 * x2 <= 18

# Résolution
prob.solve()

print("=== Exemple (Production de Châssis) ===")
print("Statut :", pulp.LpStatus[prob.status])
print(f"x1 (Châssis aluminium) = {x1.varValue}")
print(f"x2 (Châssis bois)       = {x2.varValue}")
print(f"Profit maximal Z = {pulp.value(prob.objective)} UM")

# ----- Graphique -----
x = np.linspace(0, 10, 200)
c1 = 4 * np.ones_like(x)         # x1 <= 4
c2 = 6 * np.ones_like(x)         # x2 <= 6
c3 = (18 - 3*x) / 2              # 3x1 + 2x2 = 18

plt.plot(x, c1, label="x1 = 4")
plt.plot(x, c2, label="x2 = 6")
plt.plot(x, c3, label="3x1 + 2x2 = 18")

plt.xlim(0, 10)
plt.ylim(0, 10)

# Zone faisable
plt.fill_between(x, 0, np.minimum.reduce([c1, c2, c3]), color='lightblue', alpha=0.4)

# Point optimal
plt.scatter([x1.varValue], [x2.varValue], color='red', s=80, label="Solution optimale")

plt.xlabel("x1 (Châssis aluminium)")
plt.ylabel("x2 (Châssis bois)")
plt.title("Zone Faisable + Solution Optimale")
plt.legend()
plt.grid(True)
plt.show()
