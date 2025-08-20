def derivative(x, f, h=1e-5):
    """
    Approximates the first derivative of a function at a given point
    
    Parameters:
    - x: point to evaluate the function at
    - f: function to differentiate
    - h: step size for finite difference (default: 1e-5)

    Returns:
    - result: scalar representing the derivative at x

    Other Comments: 
    - h is a small number that represents a tiny step along the x-axis (i.e, slope). It's used to approximate the derivative of a function using the finite different method, which is based on the limit definition of a derivative.
    - return statement represents the forward difference formula (although central difference is more accurate)
    """
    return (f(x + h) - f(x)) / (h)



def optimize(Xt_minus_1, f, h=1e-5, tol=1e-7):
    """
    Function for univariate Newton's method: finding a local minimum of f using finite differences.

    Parameters: 
    - Xt_minus_1: starting point
    - f: function to minimize
    - h: step size for finite difference (default: 1e-5)
    - tol: tolerace for stopping

    Returns:
    - Xt: estimated minimum point

    Embedded Functions:
    - derivative(x, f)

    Other Comments: 
    - h is a small number that represents a tiny step along the x-axis (i.e, slope). 
    It's used to approximate the derivative of a function using the finite different method, which is based on the limit definition of a derivative.
    """
    first_derivative = derivative(Xt_minus_1, f)
    second_derivative = derivative(Xt_minus_1, lambda x: derivative(x, f))
    
    Xt = Xt_minus_1 - (first_derivative / second_derivative)
        
    while (abs(Xt - Xt_minus_1) > tol):
        first_derivative = derivative(Xt, f)
        second_derivative = derivative(Xt, lambda x: derivative(x, f))
    
        Xt_plus_1 = Xt - (first_derivative / second_derivative)

        Xt_minus_1 = Xt
        Xt = Xt_plus_1
    
    return Xt


