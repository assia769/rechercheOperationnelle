import pulp
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
couts = {"poulet": 15, "canard": 10, "dindon": 40}
prix = {"poulet": 30, "canard": 20}
D = 60  # Prix du dindon

# Variables
poulet = pulp.LpVariable("Poulets", lowBound=0, cat="Integer")
canard = pulp.LpVariable("Canards", lowBound=0, cat="Integer")
dindon = pulp.LpVariable("Dindons", lowBound=0, cat="Integer")

# Définir problème
prob = pulp.LpProblem("Maximiser_Profit", pulp.LpMaximize)
prob += (prix["poulet"]*poulet + prix["canard"]*canard + D*dindon 
         - couts["poulet"]*poulet - couts["canard"]*canard - couts["dindon"]*dindon), "Profit"
prob += poulet + canard + dindon == 500
prob += canard <= 300

# Résolution
prob.solve()
x_opt = poulet.varValue
y_opt = canard.varValue
z_opt = dindon.varValue
profit_opt = pulp.value(prob.objective)

print(f"Solution optimale : Poulets={x_opt}, Canards={y_opt}, Dindons={z_opt}, Profit={profit_opt}")

# ---- Graphique ----
x = np.linspace(0, 500, 500)
y1 = 500 - x             # dindons ≥ 0
y2 = 300                  # canards ≤ 300
y_max = np.minimum(y1, y2)

plt.figure(figsize=(8,6))
plt.fill_between(x, 0, y_max, color='lightblue', alpha=0.4, label="Zone faisable")
plt.scatter(x_opt, y_opt, color='red', s=100, label="Solution optimale")
plt.xlabel("Poulets")
plt.ylabel("Canards")
plt.title(f"Zone faisable et solution optimale (D={D} F)")
plt.legend()
plt.grid(True)
plt.show()
