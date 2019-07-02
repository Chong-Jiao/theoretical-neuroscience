import numpy as np 

def estimate_response_with_linear_kernel(input, kernel, deltaT):
    N = len(input)
    r = np.zeros(input.shape)
    for i in range(N):
        x = input[i::-1].view()
        k = kernel(deltaT*np.arange(i+1)).reshape(x.shape)
        r[i] = np.sum(x*k)
    return r
