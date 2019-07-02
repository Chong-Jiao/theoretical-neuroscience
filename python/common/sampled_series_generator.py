import numpy as np
import common.sampled_series as s_series
def gauss_white_noise(duration, deltaT, sigma):
    N = int(duration/deltaT)+1
    return np.random.randn(N)*sigma/np.sqrt(deltaT)

class GaussWhiteNoiseGenerator(object):
    def __init__(self, duration, fs, sigma):
        self.duration = duration
        self.fs = fs
        self.sigma = sigma

    def generate(self):
        series = gauss_white_noise(self.duration, 1.0/self.fs, self.sigma)
        return s_series.SampledSeries(series, self.fs)
