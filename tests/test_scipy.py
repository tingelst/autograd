import autograd.numpy as np
import autograd.numpy.random as npr
import autograd.scipy.misc
import autograd.scipy.signal
import autograd.scipy.stats

from autograd import grad
from numpy_utils import combo_check, check_grads
npr.seed(1)

def test_norm_pdf():
    x = npr.randn()
    l = npr.randn()
    scale=npr.rand()**2 + 1.1
    fun = autograd.scipy.stats.norm.pdf
    d_fun = grad(fun)
    check_grads(fun, x, l, scale)
    check_grads(d_fun, x, l, scale)

def test_norm_cdf():
    x = npr.randn()
    l = npr.randn()
    scale=npr.rand()**2 + 1.1
    fun = autograd.scipy.stats.norm.cdf
    d_fun = grad(fun)
    check_grads(fun, x, l, scale)
    check_grads(d_fun, x, l, scale)

def test_norm_logpdf():
    x = npr.randn()
    l = npr.randn()
    scale=npr.rand()**2 + 1.1
    fun = autograd.scipy.stats.norm.logpdf
    d_fun = grad(fun)
    check_grads(fun, x, l, scale)
    check_grads(d_fun, x, l, scale)

R = npr.randn
def test_logsumexp1(): combo_check(autograd.scipy.misc.logsumexp, [0],
                                   [R(4), R(3,4)], axis=[None, 0])
def test_logsumexp2(): combo_check(autograd.scipy.misc.logsumexp, [0],
                                   [R(3,4), R(4,5,6)], axis=[None, 0, 1])
def test_logsumexp3(): combo_check(autograd.scipy.misc.logsumexp, [0],
                                   [R(4)], b = [np.exp(R(4))], axis=[None, 0])
def test_logsumexp4(): combo_check(autograd.scipy.misc.logsumexp, [0],
                                   [R(3,4),], b = [np.exp(R(3,4))], axis=[None, 0, 1])
def test_logsumexp5(): combo_check(autograd.scipy.misc.logsumexp, [0],
                                   [R(2,3,4)], b = [np.exp(R(2,3,4))], axis=[None, 0, 1])

def test_convolve(): combo_check(autograd.scipy.signal.convolve, [0,1],
                                 [R(4), R(5), R(6)],
                                 [R(2), R(3), R(4)],
                                 mode=['full', 'valid', 'same'])

def test_convolve2d(): combo_check(autograd.scipy.signal.convolve2d, [0, 1],
                                   [R(4, 3), R(5, 4), R(6, 7)],
                                   [R(2, 2), R(3, 2), R(4, 3)],
                                   mode=['full', 'valid', 'same'])
