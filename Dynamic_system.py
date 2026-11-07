# In world method of simulating dynamic systems in python
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
u0 = [1.0, 1.0, 1.0]

# Evaluation points
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# ODE solver algorithm
solution = solve_ivp(lorenz_system, t_span, u0, method='RK45', t_eval=t_eval)

# Extract co-ordinates
x, y, z = solution.y # Contains the 2D array of shape [3, 10000]

#Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=solution.t, cmap='plasma', s=0.5, alpha=0.8)

ax.set_title("Lorenz Attractor via SciPy solve_ivp (RK45)", fontsize=14, fontweight='bold')
ax.set_xlabel("X - Convective Intensity")
ax.set_ylabel("Y - Horizontal Temp Diff")
ax.set_zlabel("Z - Vertical Temp Distortion")
plt.show()
