"""
Nonlinear pendulum example for the RK4 solver.

This script demonstrates:

1. Solving a nonlinear pendulum equation
2. Converting a second-order ODE into a system
   of first-order ODEs
3. Time evolution of the pendulum angle
4. Time evolution of the angular velocity
5. Phase-space visualization

Author: Maryam Asghari
Version: 1.0
Date: June 2026
"""

import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
    )


import numpy as np
import matplotlib.pyplot as plt

from rk4_solver import rk4_solver

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FIGURES_DIR = PROJECT_ROOT / "figures"

FIGURES_DIR.mkdir(exist_ok=True)


def pendulum(t, y):
    
    """
    Dimensionless nonlinear pendulum model.
    
    The governing equation is

        theta'' + sin(theta) = 0

    written as the first-order system

        theta' = omega
        omega' = -sin(theta)
 
    Parameters
    ----------
    t : float
        Time.
    y : ndarray
        State vector:

            y[0] = theta
            y[1] = omega
            
    Note
    ----
    The variable t is included only to match
    the solver interface.
    
    Returns
    -------
    ndarray
        Time derivatives.
    """
    theta = y[0]
    omega = y[1]

    dydt = np.array([
        omega,
        -np.sin(theta)
    ])

    return dydt

# ----------------------------------
# Solve Pendulum Equation
# ----------------------------------

t, y = rk4_solver(
    pendulum,
    t0=0.0,
    y0=np.array([1.0, 0.0]),
    t_end=20.0,
    h=0.01
)


theta = y[:, 0]
omega = y[:, 1]

# ----------------------------------
# Print Results
# ----------------------------------

print("Nonlinear Pendulum Example")
print(f"Number of time steps = {len(t)}")
print()

print("Initial state:")
print(f"theta(0) = {theta[0]:.6f}")
print(f"omega(0) = {omega[0]:.6f}")

print()

print("Final state:")
print(f"theta(T) = {theta[-1]:.6f}")
print(f"omega(T) = {omega[-1]:.6f}")

# ----------------------------------
# Plot Theta
# ----------------------------------

plt.figure()

plt.plot(t, theta)

plt.xlabel("t")
plt.ylabel(r"$\theta$ (rad)")
plt.title("Pendulum Angle")
plt.grid(True)

plt.savefig(
    str(FIGURES_DIR / "pendulum_angle.png"),
    dpi=300,
    bbox_inches="tight"
)


# ----------------------------------
# Plot Omega
# ----------------------------------

plt.figure()

plt.plot(t, omega)

plt.xlabel("t")
plt.ylabel(r"$\omega$ (rad/s)")
plt.title("Angular Velocity")
plt.grid(True)

plt.savefig(
    str(FIGURES_DIR / "pendulum_velocity.png"),
    dpi=300,
    bbox_inches="tight"
)


# ----------------------------------
# Plot Phase Space
# ----------------------------------

plt.figure()

plt.plot(theta, omega)

plt.xlabel(r"$\theta$ (rad)")
plt.ylabel(r"$\omega$ (rad/s)")
plt.title("Pendulum Phase Space")
plt.grid(True)
plt.savefig(
    str(FIGURES_DIR / "pendulum_phase_space.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()
