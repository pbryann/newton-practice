import pytest
import numpy as np
import math

import newton

# # Important: structure of tests assumes a dictionary with an 'x'
# # key as the output. 

def test_basic_function():
    assert np.isclose(newton.optimize(2.95, np.cos)['x'], math.pi)

def test_bad_input():
    with pytest.raises(TypeError, match='Xt_minus_1 must be numeric and real.'):
        newton.optimize(np.cos, 2.95)

def test_bad_input_2():
    with pytest.raises(TypeError, match='f must be a differentiable function.'):
        newton.optimize(2.95, 1)

# # How to check that a warning is (correctly) emitted:
# # def test_warning():
# #    with pytest.warns(UserWarning, match='greater'):
# #        newton.optimize(...., ....)
