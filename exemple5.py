import pulp
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
thon_n, thon_s = 6, 30
morue_n, morue_s = 20, 8
sardine_n, sardine_s = 10, 10

quota_thon = 60
quota_morue = 60
quota_sardine = 20

# Variables : nombre de travailleurs Nord et Sud
x1 = pulp.LpVariable("Travailleurs_Nord", lowBound=0, cat="Continuous")
x2 = pulp.LpVariable("Travailleurs_Sud", lowBound=0, cat="Continuous")

# Problème : minimiser le nombre total de travailleurs
prob = pulp.LpProblem("Min_Travailleurs", pulp.LpMinimize)
prob += x1 + x2, "Nombre_total_travailleurs"

# Contraintes
prob += thon_n*x1 + thon_s*x2 >= quota_thon, "Thon_min"
prob += morue_n*x1 + morue_s*x2 >= quota_morue, "Morue_min"
prob += sardine_n*x1 + sardine_s*x2 >= quota_sardine, "Sardine_min"

# Résolution
prob.solve()

# Affichage du résultat comme demandé
print("Statut de résolution :", pulp.LpStatus[prob.status])
print(f"x1 = {x1.varValue}")
print(f"x2 = {x2.varValue}")
print(f"Valeur optimale Z = {pulp.value(prob.objective)}")

# ---- Graphique ----
x = np.linspace(0, 10, 400)
y_thon = (quota_thon - thon_n*x)/thon_s
y_morue = (quota_morue - morue_n*x)/morue_s
y_sardine = (quota_sardine - sardine_n*x)/sardine_s

y_max = np.maximum.reduce([y_thon, y_morue, y_sardine])

plt.figure(figsize=(8,6))
plt.plot(x, y_thon, label="Thon")
plt.plot(x, y_morue, label="Morue")
plt.plot(x, y_sardine, label="Sardine")
plt.fill_between(x, y_max, 15, color='lightblue', alpha=0.3, label="Zone faisable")
plt.scatter(x1.varValue, x2.varValue, color='red', s=100, label="Solution optimale")
plt.xlim(0, 10)
plt.ylim(0, 15)
plt.xlabel("Travailleurs Nord")
plt.ylabel("Travailleurs Sud")
plt.title("Zone faisable et solution optimale")
plt.legend()
plt.grid(True)
plt.show()
