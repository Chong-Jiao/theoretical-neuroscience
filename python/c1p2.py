import numpy as np 
import matplotlib.pyplot as plt
from common import spike_generators
from common import util

def p2():
    max_rate = 100
    duration = 10
    
    recovery_times = range(1, 21)
    all_spikes = [spike_generators
                  .HomogeneousPoissonGeneratorWithRefractory(max_rate, t).generate(duration) for t in recovery_times]
    cv = [s.coefficient_variation() for s in all_spikes]
    plt.figure()
    plt.bar([x-0.5 for x in recovery_times], cv, width=1, bottom=0)
    plt.xlabel('Recovery time (ms)')
    plt.ylabel('Coefficient of variation')
    plt.xlim(0, 21)
    
    for t in [0, 9, 19]:
        util.plot_interspike_interval_histogram(all_spikes[t], 
                                            title='Interspike interval ' +
                                             'histogram with recovery_time={}'.format(recovery_times[t])) 
        util.plot_spikes(all_spikes[t], figsize=(20, 1))
    
    plt.show()
    
    print("Fano factor for counting intervals in [0, 100] ms when recovery time is 10ms: \n{}".format(
            all_spikes[9].fano_factor(np.arange(1, 100))))
    
p2()