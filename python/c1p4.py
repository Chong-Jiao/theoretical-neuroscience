import numpy as np 
import matplotlib.pyplot as plt
from common import spike_generators
from common import util
from functools import partial

def p4():
    duration = 10
    
    def f1(t):
        return 100 * (1 + np.cos(2 * np.pi * t * 1000. / 300))
    def f2(t, prev_t, tau):
        return (1000.0 / tau) * np.exp(-(t - prev_t) * 1000. / tau)
    
    g1 = spike_generators.PoissonGeneratorWithVariableRate(max_rate=200, rate_fn=f1).generate(duration)
    taus = list(range(1,101))

    def average_square_error(g, tau):
        ''' estimate the error with g and actual firing rate
            tau, time constant in milliseconds
            g, generated spike train
        '''
        N = len(g.spikes)
        error = 0
        for t, t_next in zip(g.spikes, np.hstack((g.spikes[1:], g.duration))):
            sum1 = 15000*(t_next-t)+375/np.pi*(np.sin(40*np.pi*t_next/3)-np.sin(40*np.pi*t/3))+200*15/np.pi*(np.sin(20*np.pi*t_next/3)-np.sin(20*np.pi*t/3))
            sum2 = (1-np.exp(-2000*(t_next-t)/tau))*500/tau
            sum31 = -200*(1-np.exp(-1000*(t_next-t)/tau))
            m = np.pi*20/3
            n = -1000/tau
            def i1(ct):
                return np.sin(m*t)*np.exp(n*(ct-t))*m
            def i2(ct):
                return np.exp(n*(ct-t))*np.cos(m*t)*n
            ix1 = i1(t_next)-i1(t) 
            ix2 = i2(t_next)-i2(t)
            sum32 = -200*1000/tau*(ix1+ix2)/(n**2)

            error += sum1+sum2+sum31+sum32
        return error
    errors = [average_square_error( g1, tau) for tau in taus] 
    ix = np.argmin(errors)
    print('The best tau equals {}, with error={}'.format(taus[ix], errors[ix]))
    
    interval = 35

    counts = g1.spike_counts(interval)
    counts_rate = counts*1000/interval

    t = np.arange(len(counts_rate))*interval+interval/2
    rt = f1(t/1000)

    tau = taus[ix]
    appro_count_rate = np.zeros(t.shape)
    j = -1
    for i, ti in enumerate(t):
        ti = ti/1000
        while(j < len(g1.spikes)-1):
            if(ti<g1.spikes[j+1]):
                if(j<0):
                    appro_count_rate[i] = 0
                else:
                    appro_count_rate[i]=1000/tau*np.exp(-(ti-g1.spikes[j])*1000/tau)
                break
            else:
                j+=1
        if(j>=len(g1.spikes)):
            appro_count_rate[i]=1000/tau*np.exp(-(ti-g1.spikes[-1])*1000/tau)


    plt.figure()
    plt.plot(t, rt)
    plt.plot(t, counts_rate)
    plt.plot(t, appro_count_rate)
    plt.legend(('r(t)','generated_spike rate','estimated rate'))
    
    plt.show()
p4()