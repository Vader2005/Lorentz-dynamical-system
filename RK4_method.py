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

# Vectorise our Lorenz system
def lorenz_system(u):
    x, y, z = u[0], u[1], u[2] # u is a vector [x, y, z]

    # Derivatives
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = (x * y) - (beta * z)

    # Return array of derivatives
    return np.array([dxdt, dydt, dzdt])

# Storage array
trajectory = np.empty((num_steps, 3)) #3 cols: x, y, z

# Initial conditions
trajectory[0] = np.array([1.0, 1.0, 1.0])

#RK4
for n in range(num_steps-1):
    u_current = trajectory[n]

    # K equations
    k1 = lorenz_system(u_current)
    k2 = lorenz_system(u_current + (h/2.0)*k1)
    k3 = lorenz_system(u_current + (h/2.0)*k2)
    k4 = lorenz_system(u_current + h*k3)

    # Algorithm
    trajectory[n+1] = u_current + (h/6.0) * (k1 + 2*k2 + 2*k3 + k4)

# Extract co-ordinates
x = trajectory[:, 0]
y = trajectory[:, 1]
z = trajectory[:, 2]

#Visualize the results in 3D using Matplotlib
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting trajectory
ax.scatter(x, y, z, c=np.arange(num_steps), cmap='viridis', s=0.5, alpha=0.8)

# Styling
ax.set_title("Lorenz Attractor via True Coupled RK4 Method", fontsize=14, fontweight='bold')
ax.set_xlabel("X (Convective Intensity)")
ax.set_ylabel("Y (Horizontal Temp Difference)")
ax.set_zlabel("Z (Vertical Temp Distortion)")
ax.grid(True, linestyle='--', alpha=0.5)

plt.show()
