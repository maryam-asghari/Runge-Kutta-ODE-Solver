# Runge-Kutta ODE Solver

A Python implementation of the classical fourth-order Runge-Kutta (RK4) method for solving first-order ordinary differential equations (ODEs).

## Overview

This project implements the classical RK4 algorithm for initial-value problems of the form

[
y' = f(t, y)
]

with an initial condition

[
y(t_0) = y_0.
]

The solver computes the numerical solution on a uniform time grid and provides tools for:

* Numerical integration of ODEs
* Comparison with exact solutions
* Error analysis
* Convergence studies

---

## Project Structure

```text
Runge-Kutta-ODE-Solver/
│
├── rk4_solver.py
├── examples.py
│
├── figures/
│   ├── convergence.png
│   ├── solution.png
│   └── error.png
│
└── data/
```

---

## Numerical Method

The classical fourth-order Runge-Kutta method advances the solution according to

[
k_1 = f(t_n, y_n)
]

[
k_2 = f\left(t_n+\frac{h}{2},
y_n+\frac{h}{2}k_1\right)
]

[
k_3 = f\left(t_n+\frac{h}{2},
y_n+\frac{h}{2}k_2\right)
]

[
k_4 = f(t_n+h,
y_n+h k_3)
]

and

[
y_{n+1}
=======

y_n
+
\frac{h}{6}
(k_1 + 2k_2 + 2k_3 + k_4).
]

The RK4 method has a global error of order

[
O(h^4).
]

---

## Example Problem

The included example solves

[
y' = y,
]

with

[
y(0)=1.
]

The exact solution is

[
y(t)=e^t.
]

The numerical solution is compared against the analytical result.

---

## Convergence Study

A convergence test is performed using several step sizes:

```text
0.4
0.2
0.1
0.05
0.025
0.0125
0.00625
```

The measured convergence slope is approximately

```text
3.93
```

which is consistent with the theoretical fourth-order accuracy of RK4.

---

## Results

The project automatically generates:

* Numerical solution plot
* Pointwise error plot
* Convergence plot

These figures are stored in the `figures` directory.

---

## Requirements

* Python 3.x
* NumPy
* Matplotlib

Install dependencies with:

```bash
pip install numpy matplotlib
```

---

## Author

Maryam Asghari

June 2026
