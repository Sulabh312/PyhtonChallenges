x_f = 4
T = 2
u = (2 * x_f) / (T**2)
print(f"Required accelaration u = {u:.2f} m/s^2")
u_max = 5
if u > u_max:
    print("Infeasible: exceeds actuator limit")
else:
    print("Feasible: within actuator limit")