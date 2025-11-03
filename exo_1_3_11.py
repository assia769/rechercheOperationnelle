import pulp
import matplotlib.pyplot as plt
import numpy as np

prob = pulp.LpProblem("Exemple_1_3_11", pulp.LpMinimize)
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)

prob += 20 * x1 + 25 * x2
prob += x1 + 5 * x2 >= 5
prob += x1 + 2 * x2 >= 4
prob += 3 * x1 + 2 * x2 >= 6

prob.solve()

print("=== Exemple 1.3.11 ===")
print("Statut de résolution :", pulp.LpStatus[prob.status])
print(f"x1 = {x1.varValue}")
print(f"x2 = {x2.varValue}")
print(f"Valeur optimale Z = {pulp.value(prob.objective)}")
x = np.linspace(0, 5, 100)
c1 = (5 - x) / 5
c2 = (4 - x) / 2
c3 = (6 - 3 * x) / 2

plt.plot(x, c1, label="x1 + 5x2 = 5")
plt.plot(x, c2, label="x1 + 2x2 = 4")
plt.plot(x, c3, label="3x1 + 2x2 = 6")

plt.xlim(0, 5)
plt.ylim(0, 5)
plt.fill_between(x, np.maximum.reduce([c1, c2, c3]), 5, alpha=0.3, color='lightblue')
plt.scatter([x1.value()], [x2.value()], color='red', label='Optimum')
plt.legend()
plt.title("Exemple 1.3.11 - Minimisation")
plt.show()
