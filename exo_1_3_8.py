import pulp
import matplotlib.pyplot as plt
import numpy as np

prob = pulp.LpProblem("Exemple_1_3_8", pulp.LpMaximize)
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)

prob += 6 * x1 + x2
prob += x1 + 4 * x2 <= 2
prob += x1 + x2 >= 1
prob += 6 * x1 + x2 <= 2

prob.solve()

print("=== Exemple 1.3.8 ===")
print("Statut de résolution :", pulp.LpStatus[prob.status])
print(f"x1 = {x1.varValue}")
print(f"x2 = {x2.varValue}")
print(f"Valeur optimale Z = {pulp.value(prob.objective)}")

x = np.linspace(0, 1, 100)
c1 = (2 - x) / 4
c2 = 1 - x
c3 = 2 - 6 * x
plt.plot(x, c1, label="x1 + 4x2 = 2")
plt.plot(x, c2, label="x1 + x2 = 1")
plt.plot(x, c3, label="6x1 + x2 = 2")
plt.xlim(0, 1)
plt.ylim(0, 2)
plt.scatter([x1.value()], [x2.value()], color='red', label='Optimum')
plt.fill_between(x, np.maximum(c2, 0), np.minimum(c1, c3), alpha=0.3, color='lightblue')
plt.legend()
plt.title("Exemple 1.3.8 - Maximisation")
plt.show()
