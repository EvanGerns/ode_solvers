import numpy as np

def constant(t, x):
    #x=t+x0
    return 1

def linear_t(t, x):
    #x=t^2+x0
    return 2*t

def linear_x(t, x):
    #x=x0*exp(-3x)
    return -3*x

def sin_t(t, x):
    #x=2*cos(3t)
    return -6 * np.sin(3*t)

