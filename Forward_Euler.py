# Import necessary modules
import numpy as np
import matplotlib.pyplot as plt

# Define the system parameters
sigma = 10.0
rho = 28.0
beta = 8.0/3.0

# Time parameters for Euler
h = 0.005 # step size
t_max = 50.0
num_steps = int(t_max/h)

# Initialise arrays
x = np.empty(num_steps)
y = np.empty(num_steps)
z = np.empty(num_steps)

# Initial condition vector
x[0], y[0], z[0] = (1.0, 1.0, 1.0)

# Forward Euler Algorithm
for n in range(num_steps-1):
    # Derivatives
    dxdt = sigma * (y[n] - x[n])
    dydt = x[n] * (rho - z[n]) - y[n]
    dzdt = (x[n] * y[n]) - (beta * z[n])

    # Euler algorithm
    x[n+1] = x[n] + h*dxdt
    y[n+1] = y[n] + h*dydt
    z[n+1] = z[n] + h*dzdt


# Visualising in Matplotlib
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot trajectory
ax.scatter(x, y, z, c=np.arange(num_steps), cmap='plasma', s=0.5, alpha=0.8)

# Styling and labels
ax.set_title("Lorenz Attractor via Euler's Method", fontsize=14, fontweight='bold')
ax.set_xlabel("X (Convective Intensity)")
ax.set_ylabel("Y (Horizontal Temp Difference)")
ax.set_zlabel("Z (Vertical Temp Distortion)")

# Set a dark theme grid for better 3D depth perception
ax.grid(True, linestyle='--', alpha=0.5)
plt.show()
