import numpy as np
input = np.array([10, 20, -1, 0])
reversed = input[::-1]
reversed[:2]
def coef(x, y):
    """
    Determine Coefficients of a polynomial approximation Via Divided Difference Method
    Parameters:
    @param x: domain to interpolate
    @param y: range of interpolation
    y = f(x)
    """
    x.astype(float)
    y.astype(float)
    n = len(x)
    a = [value for value in y]
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = float(a[i] - a[i-1])/float(x[i]-x[i-j])
    return np.array(a)
def fit_polynomial(x, y):
    """ Return polynomial expression of order 2"""

    coeficcients = coef(x,y)[:3]

    return np.poly1d(coefficients)
