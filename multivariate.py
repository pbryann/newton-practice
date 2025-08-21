# import libraries
import numpy as np
import scipy

# more niche libraries
from scipy.differentiate import hessian
from scipy.optimize import approx_fprime

def multivariate(Xt_minus_1, f, h=1e-5, tol=1e-7):
    """
    """
    x = np.array(Xt_minus_1)

    gradient = approx_fprime(x, f, h)
    hessian_matrix = hessian(f, x, h)

    Xt = Xt_minus_1 - (gradient * hessian_matrix) 
    
    while (abs(Xt - Xt_minus_1) > tol):
        # Repeat steps ...
        gradient = approx_fprime(x, f, h)
        hessian_matrix = hessian(f, x, h)

        Xt_plus_1 = Xt - (first_derivative / second_derivative)

        # Redefine variables to prevent infinite loops
        Xt_minus_1 = Xt 
        Xt = Xt_plus_1
        
    return Xt