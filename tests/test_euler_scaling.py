import numpy as np
from src.solvers import euler
import src.equations as eqs


def test_linear_t():
    t1 = np.linspace(0, 100, 1000)
    t2 = np.linspace(0, 100, 2000) #2 times as fine --> ~1/2 the error (for sufficiently small timesteps)
    nsol1 = euler(eqs.linear_t, 1, t1)
    nsol2 = euler(eqs.linear_t, 1, t2)
    asol1 = np.power(t1, 2) + 1
    asol2 = np.power(t2, 2) + 1
    error1 = np.max(np.abs(nsol1-asol1))
    error2 = np.max(np.abs(nsol2-asol2))
    #print(error1/error2)
    assert np.abs(error1 - 2 * error2) < 0.01 * error1

def test_linear_x():
    t1 = np.linspace(0, 100, 10000)
    t2 = np.linspace(0, 100, 30000) #3 times as fine --> ~1/3 the error (for sufficiently small timesteps)
    nsol1 = euler(eqs.linear_x, 1, t1)
    nsol2 = euler(eqs.linear_x, 1, t2)
    asol1= np.exp(-3 * t1)
    asol2 = np.exp(-3 * t2)
    error1 = np.max(np.abs(nsol1-asol1))
    error2 = np.max(np.abs(nsol2-asol2))
    #print(error1/error2)
    assert np.abs(error1 - 3 * error2) < 0.01 * error1

def test_sin():
    t1 = np.linspace(0, 100, 10000)
    t2 = np.linspace(0, 100, 50000) #5 times as fine --> ~1/5 the error (for sufficiently small timesteps)
    nsol1 = euler(eqs.sin_t, 2, t1)
    nsol2 = euler(eqs.sin_t, 2, t2)
    asol1 = 2 * np.cos(3*t1)
    asol2 = 2 * np.cos(3*t2)
    error1 = np.max(np.abs(nsol1-asol1))
    error2 = np.max(np.abs(nsol2-asol2))
    #print(error1/error2)
    assert np.abs(error1 - 5 * error2) < 0.01 * error1

#test_linear_t()
#test_linear_x()
#test_sin()
