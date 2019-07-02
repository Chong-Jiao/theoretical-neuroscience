import numpy as np 

def xcorr(x, y,maxlag=None,lags=None, option='unbiased'):
    N = len(x)
    assert(N == len(y))
    x = x-np.mean(x)
    y = y-np.mean(y)
    if(lags is None):
        if(maxlag is None):
            maxlag = int(N*0.15)
        lags = np.arange(2*maxlag+1)-maxlag
    corr = np.zeros(lags.shape)
    for i in range(len(lags)):
        lag = lags[i]
        if(lag>0):
            xs = x[:-lag]
            ys = y[lag:]
        elif(lag<0):
            xs = x[-lag:]
            ys = y[:lag]
        else:
            xs = x
            ys = y
        corr[i] = np.sum(xs*ys)
    
    if(option == 'unbiased'):
        items = N-np.abs(lags)
        corr = corr/items
    else:
        corr = corr/N
    return corr, lags
