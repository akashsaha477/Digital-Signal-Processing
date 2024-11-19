import numpy as np


x = [1, 2, 3]
h = [0, 1, 0.5]


def manual_correlation(x, h):
   
    h_reversed = h[::-1]
    
   
    len_x = len(x)
    len_h = len(h_reversed)
    
    len_y = len_x + len_h - 1
    
   
    y = [0] * len_y
    
   
    for n in range(len_y):
        for k in range(len_x):
            if 0 <= n - k < len_h:
                y[n] += x[k] * h_reversed[n - k]
    
    return y


def inbuilt_correlation(x, h):
    return np.correlate(x, h, mode='full')

y_manual = manual_correlation(x, h)


y_inbuilt = inbuilt_correlation(x, h)


print("Manual Correlation:", y_manual)
print("Inbuilt Correlation:", y_inbuilt.tolist())
