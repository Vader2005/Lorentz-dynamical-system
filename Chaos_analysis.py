# Import modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define constants
sigma = 10.0
rho = 28.0
beta = 8.0/3.0

# Define our system/ode
def lorenz_system(t, u): # Scipy always requires t as first argument
    x, y, z = u
    dxdt = sigma * (y - x)
    dydt = x*(rho - z) - y
    dzdt = (x*y) - (beta*z)

    return [dxdt, dydt, dzdt]

# Boundary conditions and Initial conditions
t_span = (0.0, 50.0) # time interval
u0_base = [1.0, 1.0, 1.0]
u0_perturbed = [1.0, 1.0, 1.00001] # 10^-5 difference in Z

# Evaluation points
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# ODE solver algorithm
sol_base = solve_ivp(lorenz_system, t_span, u0_base, method='RK45', t_eval=t_eval, rtol=1e-10)
sol_pert = solve_ivp(lorenz_system, t_span, u0_perturbed, method='RK45', t_eval=t_eval, rtol=1e-10)

# Euclidean distance of points
delta = sol_base.y - sol_pert.y
distance = np.linalg.norm(delta, axis=0)

# Plot the log of the distance
plt.figure(figsize=(10, 5))
plt.plot(sol_base.t, np.log(distance), color='darkblue', linewidth=1.5)

# Style the graph
plt.title("Mathematical Signature of Chaos (Lyapunov Growth)", fontsize=12, fontweight='bold')
plt.xlabel("Time (t)")
plt.ylabel("Log of Separation Distance:  $\ln(d)$")
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
