import pulp
import matplotlib.pyplot as plt
import numpy as np

# Définir le problème
prob = pulp.LpProblem("Exemple_1_3_7", pulp.LpMaximize)

x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)

# Fonction objectif
prob += 3 * x1 + x2

# Contraintes
prob += 3 * x1 - x2 >= 3
prob += x1 + x2 <= 1

# Résolution
prob.solve()

print("=== Exemple 1.3.7 ===")
print("Statut de résolution :", pulp.LpStatus[prob.status])
print(f"x1 = {x1.varValue}")
print(f"x2 = {x2.varValue}")
print(f"Valeur optimale Z = {pulp.value(prob.objective)}")





# ----- Graphique -----
x = np.linspace(0, 4, 100)
c1 = 3 * x - 3
c2 = 1 - x

plt.plot(x, c1, label="3x1 - x2 = 3")
plt.plot(x, c2, label="x1 + x2 = 1")

plt.xlim(0, 4)
plt.ylim(0, 4)
plt.fill_between(x, np.maximum(c1, 0), c2, where=(c2 >= c1), alpha=0.3, color='lightblue')

plt.scatter([x1.value()], [x2.value()], color='red', label='Optimum')
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.title("Exemple 1.3.7 - Maximisation")
plt.show()
