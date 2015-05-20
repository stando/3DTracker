__author__ = 'stando'

import numpy
import nose

def heaviside(x):
    """
    heaviside step function
    :param x: input floating point number
    :return: 0 / 0.5 / 1
    """
    return 0.5*(numpy.sign(x) + 1)

def dirac(x):
    """
    Dirac delta function
    :param x: input floating point number
    :return: 0 / +inf
    """
    if numpy.isclose(x, 0):
        return float("inf")
    else:
        return 0
