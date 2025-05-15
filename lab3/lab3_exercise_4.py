import numpy as np

def custom_convolution(x, n_x, h, n_h):
    len_x = len(x)
    len_h = len(h)
    
    # Output length and range
    len_y = len_x + len_h - 1
    n_y = np.arange(min(n_x) + min(n_h), max(n_x) + max(n_h) + 1)
    
    # Folding 
    h_folded = np.flip(h)
    
    # Initialize the output sequence
    y = np.zeros(len_y)
    
    # Perform convolution
    for i in range(len_y):
        for j in range(len_x):
            k = i - j
            if k >= 0 and k < len_h:
                y[i] += x[j] * h_folded[k]
    
    return y, n_y


def builtin_convolution(x, h):
   
    y = np.convolve(x, h, mode='full')
    n_y = np.arange(-len(y) + 1, len(y))
    return y, n_y

# Given sequences
x = np.array([1, 5, 3, 1, 1])
n_x = np.arange(-1, 3)  

h = np.array([1, 2, 1, 2])
n_h = np.arange(-2, 2)  

# Convolution without using inbuilt function
y_custom, n_y_custom = custom_convolution(x, n_x, h, n_h)

# Convolution using inbuilt numpy function
y_builtin, n_y_builtin = builtin_convolution(x, h)

# Results
print("Custom Convolution y(n):", y_custom)
print("Custom Convolution n:", n_y_custom)

print("Built-in Convolution y(n):", y_builtin)
print("Built-in Convolution n:", n_y_builtin)

