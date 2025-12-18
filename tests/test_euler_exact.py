import numpy as np
from src.solvers import euler
import src.equations as eqs

def test_constant():
    t = np.linspace(0, 100, 1000)
    nsol = euler(eqs.constant, 0, t)
    asol = t
    assert np.allclose(nsol, asol, atol=0, rtol=0.01)

def test_linear_t():
    t = np.linspace(0, 100, 100000)
    nsol = euler(eqs.linear_t, 1, t)
    asol = np.power(t, 2) + 1
    assert np.allclose(nsol, asol, atol=0.01, rtol=0.01)

def test_linear_x():
    t = np.linspace(0, 100, 100000)
    nsol = euler(eqs.linear_x, 1, t)
    asol = np.exp(-3 * t)
    assert np.allclose(nsol, asol, atol=0.01, rtol=0.01)

def test_sin():
    t = np.linspace(0, 100, 100000)
    nsol = euler(eqs.sin_t, 2, t)
    asol = 2 * np.cos(3*t)
    assert np.allclose(nsol, asol, atol=0.01, rtol=0.01)