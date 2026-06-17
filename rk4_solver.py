"""
Fourth-order Runge-Kutta (RK4) solver for
ordinary differential equations (ODEs).

This module implements the classical
fourth-order Runge-Kutta method for solving
initial-value problems of the form

    y' = f(t, y)

where y may be either a scalar variable
or a vector of variables.

The solver supports both single ordinary
differential equations and systems of
first-order ordinary differential equations.

Given an initial condition

    y(t0) = y0

the numerical solution is computed on a
uniform time grid and returned together
with the corresponding time values.

Author: Maryam Asghari
Version: 2.0
Date: June 2026
"""

import numpy as np


def rk4_step(f, t, y, h):

    
    """
    Perform a single fourth-order
    Runge-Kutta (RK4) integration step.

 
    Parameters
    ----------
    f : callable
        Right-hand side of the ODE y' = f(t,y).
    t : float
        Current time.
    y : float or ndarray
        Current solution value.
    h : float
        Time-step size.

    Returns
    -------
    float or ndarray
        Solution after one RK4 step. 
    """    

    k1 = f(t, y)

    k2 = f(
        t + h/2,
        y + h*k1/2
    )

    k3 = f(
        t + h/2,
        y + h*k2/2
    )

    k4 = f(
        t + h,
        y + h*k3
    )

    y_new = y + h*(k1 + 2*k2 + 2*k3 + k4)/6

    return y_new

def rk4_solver(f, t0, y0, t_end, h):


    """
    Solve a first-order ordinary differential equation
    or a system of first-order ordinary differential
    equations using the classical RK4 method.

    
    Parameters
    ----------
    f : callable
        Right-hand side of the ODE y' = f(t, y).
    t0 : float
        Initial time.
    y0 : float or array_like
        Initial condition.
    t_end : float
        Final time.
    h : float
        Time-step size.

    Returns
    -------
    t_values : ndarray
        Discrete time grid.
    y_values : ndarray
        Numerical solution at each time point.
        For systems of equations, each row
        corresponds to one time step and each
        column corresponds to one state variable.
    """ 
    y0 = np.atleast_1d(y0)

    m = y0.size 


    N = int((t_end - t0) / h)

    t_values = np.zeros(N + 1)
    y_values = np.zeros((N + 1, m))

    t_values[0] = t0
    y_values[0] = y0

    t = t0
    y = y0

 
    for i in range(N):
         y = rk4_step(f, t, y, h)
         t = t + h

         t_values[i + 1] = t
         y_values[i + 1] = y

    return t_values, y_values 
    
