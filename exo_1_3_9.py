import pulp
import matplotlib.pyplot as plt
import numpy as np

prob = pulp.LpProblem("Exemple_1_3_9", pulp.LpMaximize)
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)

prob += 2 * x1 + 4 * x2
prob += x1 + 3 * x2 <= 18
prob += x1 + x2 <= 8
prob += 2 * x1 + x2 <= 14

prob.solve()

print("=== Exemple 1.3.9 ===")
print("Statut de résolution :", pulp.LpStatus[prob.status])
print(f"x1 = {x1.varValue}")
print(f"x2 = {x2.varValue}")
print(f"Valeur optimale Z = {pulp.value(prob.objective)}")

x = np.linspace(0, 10, 100)
c1 = (18 - x) / 3
c2 = 8 - x
c3 = 14 - 2 * x

plt.plot(x, c1, label="x1 + 3x2 = 18")
plt.plot(x, c2, label="x1 + x2 = 8")
plt.plot(x, c3, label="2x1 + x2 = 14")

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.fill_between(x, 0, np.minimum(np.minimum(c1, c2), c3), alpha=0.3, color='lightblue')
plt.scatter([x1.value()], [x2.value()], color='red', label='Optimum')
plt.legend()
plt.title("Exemple 1.3.9 - Maximisation")
plt.show()
