import numpy as np
import matplotlib.pyplot as plt
import math


def xofn(n):
    if(n<2):
        return 0
    else:
        return (0.5)**(n-2)
    
def d_sig (no_of_samples, f_of_x, st_index):
    y=np.zeros(no_of_samples)
    n=np.arange(st_index, st_index + no_of_samples)
    for i in range(no_of_samples):
        y[i]=f_of_x(st_index + 1)
    return y,n 


x, n = d_sig(30, xofn, 0)


def pole_zero(pole,zero,st_index,lem,no_of_samples):
    n=np.arange(st_index, st_index + lem)
    y=np.zeros(lem)
    for i in range(lem):
      y[i]=math.sqrt(1-(i**2))

    y[pole]=0
    y[-pole]=0
    y[zero]=0
    y[-zero]=0
    return y



