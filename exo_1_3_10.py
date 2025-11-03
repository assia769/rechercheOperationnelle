import pulp
import matplotlib.pyplot as plt
import numpy as np

prob = pulp.LpProblem("Exemple_1_3_10", pulp.LpMinimize)
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)

prob += -x1 + x2
prob += x1 + x2 >= 2
prob += 2 * x1 + x2 >= 3

prob.solve()

print("=== Exemple 1.3.10 ===")
print("Statut de résolution :", pulp.LpStatus[prob.status])
print(f"x1 = {x1.varValue}")
print(f"x2 = {x2.varValue}")
print(f"Valeur optimale Z = {pulp.value(prob.objective)}")
x = np.linspace(0, 3, 100)
c1 = 2 - x
c2 = 3 - 2 * x

plt.plot(x, c1, label="x1 + x2 = 2")
plt.plot(x, c2, label="2x1 + x2 = 3")

plt.xlim(0, 3)
plt.ylim(0, 3)
plt.fill_between(x, np.maximum(c1, c2), 3, alpha=0.3, color='lightblue')
plt.scatter([x1.value()], [x2.value()], color='red', label='Optimum')
plt.legend()
plt.title("Exemple 1.3.10 - Minimisation")
plt.show()
