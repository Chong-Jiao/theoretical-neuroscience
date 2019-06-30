import unittest

from common.sampled_series import *

class TestSampledSeries(unittest.TestCase):
    def test_duration(self):
        s = SampledSeries([1,1,1], 1)
        self.assertAlmostEqual(s.duration(), 2)