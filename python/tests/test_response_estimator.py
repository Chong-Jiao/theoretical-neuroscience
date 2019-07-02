import unittest
import numpy as np
from common.response_estimator import *

class TestResponseEstimator(unittest.TestCase):
    def test_linear_response(self):
        input = np.array([1,1,1])
        kernel = lambda tau: tau
        r = estimate_response_with_linear_kernel(input, kernel, 2)
        self.assertListEqual(list(r), [0,2,6])