import numpy as np

def euler(f, x0, t):
    """Use the forward Euler method to solve first-order ODEs of the form dx/dt = f(t, x) given initial condition x(0)=x0"""
    #f=f(t, x) is a function (dx/dt, in terms of x and t)
    #x0 is a number
    #t is an array
    x = np.zeros_like(t)
    x[0] = x0
    for index in range(1, len(t)):
        dt = t[index] - t[index-1]  #Supports non-uniform time steps
        x[index] = x[index-1] + f(t[index-1], x[index-1]) * dt
    return x


def rk2(f, x0, t):
    """Use the second-order Runge-Kutta method to solve first-order ODEs of the form dx/dt = f(t, x) given initial condition x(0)=x0"""
    x = np.zeros_like(t)
    x[0] = x0
    for index in range(1, len(t)):
        dt = t[index] - t[index-1]  #Supports non-uniform time steps
        k1 = dt * f(t[index-1], x[index-1])
        k2 = dt * f(t[index-1] + dt, x[index-1] + k1)
        x[index] = x[index-1] + (k1 + k2)/2
    return x

def rk4(f, x0, t):
    """Use the fourth-order Runge-Kutta method to solve first-order ODEs of the form dx/dt = f(t, x) given initial condition x(0)=x0"""
    x = np.zeros_like(t)
    x[0] = x0
    for index in range(1, len(t)):
        dt = t[index] - t[index-1]  #Supports non-uniform time steps
        k1 = f(t[index-1], x[index-1])
        k2 = f(t[index-1] + dt/2, x[index-1] + k1 * dt/2)
        k3 = f(t[index-1] + dt/2, x[index-1] + k2 * dt/2)
        k4 = f(t[index-1] + dt, x[index-1] + k3 * dt)
        x[index] = x[index-1] + (k1 + 2*k2 + 2*k3 + k4) * dt/6
    return x