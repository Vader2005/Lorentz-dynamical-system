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
