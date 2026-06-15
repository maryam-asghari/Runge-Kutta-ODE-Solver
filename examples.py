"""
Example scripts for the RK4 solver.

This file demonstrates:

1. Numerical solution of y' = y
2. Comparison with the exact solution
3. Error analysis
4. Convergence study of the RK4 method

Author: Maryam Asghari
Version: 1.0
Date: June 2026
"""
import os
import numpy as np
import matplotlib.pyplot as plt

from rk4_solver import rk4_solver

os.makedirs("figures", exist_ok=True)
os.makedirs("data", exist_ok=True)


def f(t, y):

    """
    Test problem:

        y' = y

    Exact solution:

        y(t) = exp(t)
    """
    
    
    return y

# ----------------------------------
# Convergence Study
# ----------------------------------

h_values = [
    0.4,
    0.2,
    0.1,
    0.05,
    0.025,
    0.0125,
    0.00625
    ]

errors = []

for h in h_values:
    
    t, y_num = rk4_solver(
        f,
        t0=0.0,
        y0=1.0,
        t_end=2.0,
        h=h
    )
    y_exact = np.exp(t)

    error = np.max(
       np.abs(y_num - y_exact)
    )

    errors.append(error)

logh = np.log(h_values)
logError = np.log(errors)




slope, intercept = np.polyfit(
    logh,
    logError,
    1 )


print()
print("RK4 Convergence Test")
print(f"Slope = {slope:.3f}")
print(f"Intercept = {intercept:.3f}")

for h, err in zip(h_values, errors):

    print(
        f"h = {h:8.5f}   "
        f"error = {err:.6e}"
    )            

   

plt.figure()

plt.plot(
    logh,
    logError,
    'o-',
    label=f"Slope = {slope:.3f}" )

plt.legend()
plt.xlabel('log(h)')
plt.ylabel('log(Error)')

plt.title("RK4 Convergence ")
plt.grid(True)


plt.savefig(
    "figures/convergence.png",
    dpi=300,
    bbox_inches="tight"
)


# ----------------------------------
# Example Solution
# ----------------------------------

t, y_num = rk4_solver(
    f,
    0.0,
    1.0,
    2.0,
    0.1
)


y_exact = np.exp(t)

plt.figure()

plt.plot(
    t,
    y_num,
    'o-',
    markersize=5,
    label='RK4'
)

plt.plot(
    t,
    y_exact,
    '-',
    linewidth=1.5,
    label='Exact'
)

plt.xlabel("t")
plt.ylabel("y")
plt.title("Solution of y'=y")
plt.legend()
plt.grid(True)


plt.savefig(
    "figures/solution.png",
    dpi=300,
    bbox_inches="tight"
)

# ----------------------------------
# Error Plot
# ----------------------------------

pointwise_error = np.abs(
    y_num - y_exact
)

plt.figure()

plt.plot(
    t,
    pointwise_error,
    'o-'
)

plt.xlabel("t")
plt.ylabel("Absolute Error")
plt.title("RK4 Error")
plt.grid(True)

plt.savefig(
    "figures/error.png",
    dpi=300,
    bbox_inches="tight"
)



    





plt.show()
