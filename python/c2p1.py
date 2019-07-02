import numpy as np
import matplotlib.pyplot as plt

from common.sampled_series_generator import *
from common.response_estimator import *
from common.basic_functions import *

import matplotlib.pyplot as plt

deltaT = 10 # in ms
fs = 1000/deltaT
sigma = np.sqrt(10)
duration = 10
r0 = 50

def D(tau):
    '''
    tau, delay time in milliseconds
    '''
    return -np.cos((2*np.pi*(tau-20))/140) * np.exp(-tau/60)

s = GaussWhiteNoiseGenerator(duration,fs,sigma).generate()

r = r0+estimate_response_with_linear_kernel(s.series, D, deltaT)

lags = np.array(range(15),dtype=np.int16)

qrs,_ = xcorr(s.series,r, lags=lags)

plt.figure()
plt.plot(lags*deltaT, D(lags*deltaT))
plt.plot(lags*deltaT,deltaT/1000*qrs/(sigma**2))
plt.legend((r'$D(\tau)$', r'$Q_{rs}(\tau)/\sigma^2$'))
plt.xlabel(r'$\tau$ (ms)')
plt.title(r'The comparison of $D(\tau)$ and $Q_{rs}(\tau)/\sigma^2$')
plt.yticks(ticks=[-1,-0.5,0,0.5,1])
plt.ylim([-1,1])
plt.show()