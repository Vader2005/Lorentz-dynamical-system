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

#Plotting: Stacked individual time-series graphs
# We create 3 rows and 1 column of subplots sharing the same X-axis (time)
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# Plot X(t) - Convective Intensity
ax1.plot(solution.t, x, color='crimson', linewidth=1)
ax1.set_ylabel("X (Convective Intensity)")
ax1.set_title("Lorenz Attractor Variables Against Time", fontsize=14, fontweight='bold')
ax1.grid(True, linestyle='--', alpha=0.5)

# Plot Y(t) - Horizontal Temp Difference
ax2.plot(solution.t, y, color='teal', linewidth=1)
ax2.set_ylabel("Y (Horizontal Temp Diff)")
ax2.grid(True, linestyle='--', alpha=0.5)

# Plot Z(t) - Vertical Temp Distortion
ax3.plot(solution.t, z, color='purple', linewidth=1)
ax3.set_ylabel("Z (Vertical Temp Distortion)")
ax3.set_xlabel("Time (t)")
ax3.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust the spacing so labels don't overlap
plt.tight_layout()
plt.show()
