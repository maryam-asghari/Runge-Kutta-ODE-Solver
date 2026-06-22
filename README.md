# Runge-Kutta ODE Solver

A Python implementation of the classical fourth-order Runge-Kutta (RK4) method for solving ordinary differential equations (ODEs).

## Overview

This project implements the classical RK4 algorithm for initial-value problems of the form

```
y' = f(t, y)
```

where y may be either a scalar variable or a vector of variables.

The solver supports:

* Single first-order ordinary differential equations
* Systems of first-order ordinary differential equations
* Error analysis
* Convergence studies
* Visualization of numerical solutions


This project was developed as a learning and portfolio project for numerical methods and scientific computing in Python.

---

## Project Structure

```text
Runge-Kutta-ODE-Solver/
│
├── rk4_solver.py
│
├── examples/
│   ├── exponential_growth.py
│   └── pendulum_example.py
│
├── figures/     
│
├── README.md
└── .gitignore
```
---

## Running the Examples

Run the exponential growth example:

```bash
python examples/exponential_growth.py
```

Run the nonlinear pendulum example:

```bash
python examples/pendulum_example.py
```

---

## Numerical Method

The classical fourth-order Runge-Kutta method advances the solution using four intermediate slope evaluations:

```
k1 = f(tn, yn)

k2 = f(tn + h/2, yn + h*k1/2)

k3 = f(tn + h/2, yn + h*k2/2)

k4 = f(tn + h, yn + h*k3)
```

and

```
yn+1 = yn + h*(k1 + 2*k2 + 2*k3 + k4)/6
```

The RK4 method has global accuracy of order

```
O(h^4)
```

---

## Included Examples

### 1. Exponential Growth

Solves

```
y' = y
```

with

```
y(0) = 1
```

The numerical solution is compared with the exact solution

```
y(t) = e^t
```

This example includes:

* Solution plot
* Error plot
* Convergence study

---

### 2. Nonlinear Pendulum

Solves the dimensionless nonlinear pendulum equation

```
θ'' + sin(θ) = 0
```

which is rewritten as the first-order system

```
θ' = ω

ω' = -sin(θ)
```

This example demonstrates:

* Solving systems of ODEs
* Time evolution of the pendulum angle and angular velocity
* Phase-space visualization

---

## Generated Figures

The example scripts automatically generate figures such as:

* Exponential growth solution
* Exponential growth error
* RK4 convergence study
* Pendulum angle
* Pendulum angular velocity
* Pendulum phase space

All figures are stored in the `figures` directory.

---

## Requirements

* Python 3.10+
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
