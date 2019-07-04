import numpy as np 
import matplotlib.pyplot as plt
from common import spike_generators
from common import util

def p3():
    duration = 10
    g1 = spike_generators.HomogeneousPoissonGenerator(200).generate(duration)
    g2 = spike_generators.HomogeneousPoissonGeneratorWithRefractory(max_rate=200, recovery_time=10).generate(duration)
    g3 = spike_generators.PoissonGeneratorWithVariableRate(max_rate=200,
             rate_fn=lambda t: 100 * (1 + np.cos(2 * np.pi * t * 1000.) / 25)).generate(duration)
            
    util.plot_autocorrelation_histogram(g1, bin_size=0.001, bin_count=100, title='Autocorrelation - g1')
    util.plot_autocorrelation_histogram(g2, bin_size=0.001, bin_count=100, title='Autocorrelation - g2')
    util.plot_autocorrelation_histogram(g3, bin_size=0.001, bin_count=100, title='Autocorrelation - g3')
    plt.show()
p3()