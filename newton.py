def derivative(x, f, h=1e-5):
    """
    Approximates the derivative of a function at a given point.
    
    Parameters:
    - x: point to evaluate the function at
    - f: function to differentiate
    - h: step size for finite difference (default: 1e-5)

    Returns:
    - Limit definition of a derivative for the function, evaluated at x

    Other Comments: 
    - h is a small number that represents a tiny step along the x-axis (i.e, slope). It's used to approximate the derivative of a function using the finite different method, which is based on the limit definition of a derivative.
    - return statement represents the forward difference formula (although central difference is more accurate)
    """
    return (f(x + h) - f(x)) / (h) # # Return statement returns limit definition of a derivative for the function, evaluated at x



def optimize(Xt_minus_1, f, h=1e-5, tol=1e-7):
    """
    Function for univariate Newton's method: Finds the root of a single-variable (univariate) function. 

    Parameters: 
    - Xt_minus_1: starting point
    - f: function to minimize
    - h: step size for finite difference (default: 1e-5)
    - tol: tolerace for stopping

    Returns:
    - Xt: estimated root 

    Embedded Functions:
    - derivative(x, f)

    Other Comments: 
    - h is a small number that represents a tiny step along the x-axis (i.e, slope). It's used to approximate the derivative of a function using the finite different method, which is based on the limit definition of a derivative.
    - About lambda: A lambda function in Python is a quick way to define a small function without giving it a name.
    """
    # Initializing ... 
    
    first_derivative = derivative(Xt_minus_1, f) 
    second_derivative = derivative(Xt_minus_1, lambda x: derivative(x, f)) # Second argument is a function representing the first derivative

    Xt = Xt_minus_1 - (first_derivative / second_derivative) # Calc Newton's method
        
    while (abs(Xt - Xt_minus_1) > tol): # Stop when Xt - Xt_minus_1 is small 
        # Repeat steps ...
        first_derivative = derivative(Xt, f)
        second_derivative = derivative(Xt, lambda x: derivative(x, f))

        Xt_plus_1 = Xt - (first_derivative / second_derivative)

        # Redefine variables to prevent infinite loops
        Xt_minus_1 = Xt 
        Xt = Xt_plus_1
    
    return Xt


