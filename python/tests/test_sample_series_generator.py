import unittest

from common.sampled_series_generator import *

class TestSampledSeries(unittest.TestCase):
    def test_gauss_white(self):
        g = GaussWhiteNoiseGenerator(10,1,1)
        self.assertAlmostEqual(g.generate().duration(), 10)