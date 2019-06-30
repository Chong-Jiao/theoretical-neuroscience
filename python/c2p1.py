import numpy as np
import matplotlib.pyplot as plt

from common.sampled_series_generator import *
import matplotlib.pyplot as plt

deltaT = 10 # in ms
fs = 1000/deltaT
sigma = np.sqrt(10)
duration = 10

def D(tau):
    '''
    tau, delay time in milliseconds
    '''
    return -np.cos((2*np.pi*(tau-20))/140) * np.exp(-tau/60)

s = GaussWhiteNoiseGenerator(duration,fs,sigma).generate()

tau = np.linspace(0,300, 500)
y = D(tau)

plt.plot(tau, y)
plt.show()
