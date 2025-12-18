import numpy as np
from src.solvers import rk4
import src.equations as eqs

def test_constant():
    t = np.linspace(0, 100, 10000)
    nsol = rk4(eqs.constant, 0, t)
    asol = t
    assert np.allclose(nsol, asol, atol=0, rtol=0.001)

def test_linear_t():
    t = np.linspace(0, 100, 10000)
    nsol = rk4(eqs.linear_t, 1, t)
    asol = np.pow(t, 2) + 1
    assert np.allclose(nsol, asol, atol=0, rtol=0.001)

def test_linear_x():
    t = np.linspace(0, 100, 10000)
    nsol = rk4(eqs.linear_x, 1, t)
    asol = np.exp(-3 * t)
    assert np.allclose(nsol, asol, atol=0, rtol=0.001)

def test_sin():
    t = np.linspace(0, 100, 10000)
    nsol = rk4(eqs.sin_t, 2, t)
    asol = 2 * np.cos(3*t)
    assert np.allclose(nsol, asol, atol=0, rtol=0.001)