import unittest

from common.spike_generators import *


class TestSpikeGenerator(unittest.TestCase):
    def test_constant_poisson_rate(self):
        tocs = poisson_constant_rate(10, 10)
        self.assertTrue(tocs[0]>0)
    def test_poisson_time_dependent_rate(self):
        tocs = poisson_time_dependent_rate(10,lambda x,y:10, 10)
        self.assertTrue(tocs[0]>0)

    def test_HomogeneousPoissonGenerator(self):
        generator = HomogeneousPoissonGenerator(100)
        duration = 10
        spike_train = generator.generate(duration)
        self.assertEqual(spike_train.duration, duration,msg='The duration should be equal to defined duration')



if __name__ == '__main__':
    unittest.main()