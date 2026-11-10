# The Lorenz Attractor

The Lorenz attractor equations are defined by this nonlinear system of first-order ordinary differential equations (ODEs):

$$
\begin{aligned}
\frac{dx}{dt} &= \sigma(y - x) \\
\frac{dy}{dt} &= x(\rho - z) - y \\
\frac{dz}{dt} &= xy - \beta z
\end{aligned}
$$

The system essentially models atmospheric convection. Because this system cannot be solved analytically, we will solve it numerically using the **Euler method** and the **RK4 (Runge-Kutta 4th Order) method**. 

---

### Variables & Physical Meaning
The states $x(t)$, $y(t)$, and $z(t)$ represent the physical properties of a fluid layer being heated from below:

* **$x(t)$** — The speed/rate at which the air rolls (convective intensity).
* **$y(t)$** — The horizontal temperature difference between ascending and descending fluids.
* **$z(t)$** — The vertical temperature profile distortion (how much it deviates from linear equilibrium).

### System Parameters (Constants)
* **$\sigma$ (Sigma)** — The Prandtl number, relating the fluid's kinematic viscosity to its thermal diffusivity.
* **$\rho$ (Rho)** — The Rayleigh number, representing the temperature difference driving the convection.
* **$\beta$ (Beta)** — A geometric factor representing the physical dimensions and aspect ratio of the fluid layer.

---

### Our system Parameters
We will be solving the classic Lorenz attractor problem with these conditions:
\
**$x(0) = 1$** \
**$y(0) = 1$** \
**$z(0) = 1$** \
**$\sigma = 10$** \
**$\rho = 28$** \
**$\beta = \frac{8}{3}$**

--- 

### Forward Euler Method

This is a 1-node quadrature method and is used to solve the problem: \
\
**$\frac{dy}{dt} = f(t, y)$** with **$y(t_0) = y_0$** and **$y(t_n) = ?$** \
\
The forward Euler method is defined as: 
\
**$y_{n+1} = y_n + hf(t_n, y_n)$**, where h is the step size.

The Forward Euler method however, becomes very unstable with a larger step size. If its amplification factor gets too large, it causes the numerical error to increase rather than decay. 

### Applying Forward Euler Method to our problem

Applying the approximation above to our system, we get these equations: \
\
**$x_{n+1} = x_n + h(\sigma(y_n - x_n))$** \
**$y_{n+1} = y_n + h(x_n(\rho - z_n) - y_n)$** \
**$z_{n+1} = z_n + h(x_ny_n - \beta*z_n)$**

---

### Rk4 Method for our problem

An extremely accurate method for approximating ODE's is the RK4 method, which is based on Simpson's quadrature rule and, for our problem:

$$
\mathbf{f}(\mathbf{u}) = \begin{bmatrix} \sigma(y - x) \\\ x(\rho - z) - y \\\ xy - \beta z \end{bmatrix}
$$

**$\vec{**k_1**} = \vec{**f**} (\vec{**u_n**})$** \
**$\vec{**k_2**} = \vec{**f**} (\vec{**u_n**} + \frac{h\vec{**k_1**}}{2})$** \
**$\vec{**k_3**} = \vec{**f**} (\vec{**u_n**} + \frac{h\vec{**k_2**}}{2})$** \
**$\vec{**k_4**} = \vec{**f**} (\vec{**u_n**} + h\vec{**k_3**})$** \
**$\vec{**u_{n+1}**} = \vec{**u_n**} + \frac{h(\vec{**k_1**} + 2\vec{**k_2**} + 2\vec{**k_3**} + \vec{**k_4**})}{6}$**

This method, unlike the Forward Euler method, can handle larger step sizes and still simulate the system with high accuracy
