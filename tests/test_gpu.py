import autograd.numpy.random as npr
import autograd.numpy as np
import operator as op
from numpy_utils import (combo_check, stat_check, unary_ufunc_check,
                         binary_ufunc_check, binary_ufunc_check_no_same_args)

npr.seed(0)

def R(*shape):
    arr = npr.randn(*shape)
    return np.array(arr, dtype=np.gpu_float32)

def test_dot(): combo_check(np.dot, [0, 1],
                            [1.5, R(3), R(2, 3)],
                            [0.3, R(3), R(3, 4)])