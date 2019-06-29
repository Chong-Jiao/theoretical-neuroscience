import unittest
import numpy as np
from common.spike_train import *

class TestSpikeTrain(unittest.TestCase):
    def test_spike_train(self):
        st = SpikeTrain(np.array([1,2,3,4,5]), 5)
        interval = 2000
        interval_counts = st.spike_counts(interval) # should be array([1,2,2])
        self.assertEqual(len(interval_counts), 3, 'should be divided into 3 counts')
        self.assertListEqual(interval_counts.tolist(),[1,2,2])
    def test_autocorrelation(self):
        st = SpikeTrain(np.array([1,2]), 2)
        binsize = 1
        bins, v= st.autocorrelation(binsize)
        self.assertListEqual(bins.tolist(), [0,1,2])
        self.assertListEqual(v.tolist(),[0,0,-1] )
