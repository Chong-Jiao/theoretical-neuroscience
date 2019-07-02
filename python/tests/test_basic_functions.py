import unittest
import numpy as np
from common.basic_functions import *

class TestBasicFunctions(unittest.TestCase):
    def test_xcorr(self):
        x = np.array([1,1,0])
        y = np.array([1,0,1])
        xy,lags = xcorr(x,y,1)
        self.assertEqual(len(xy), 3)
        self.assertListEqual(list(lags), [-1, 0, 1])
        self.assertAryAlmostEqual(list(xy), [5/18,-1/9,-1/18])
        xy,_ = xcorr(x,y,1,option='biased')
        self.assertAryAlmostEqual(list(xy), [5/27,-1/9,-1/27])
    
    def assertAryAlmostEqual(self, list1, list2, msg=None):
        for index,vs in enumerate(zip(list1, list2)):
            self.assertAlmostEqual(vs[0], vs[1],msg='The {:d}th in list didnot equal with each other, error msg={}'.format(index,msg))

if __name__ == "__main__":
    unittest.main()