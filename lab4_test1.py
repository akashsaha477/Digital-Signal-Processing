import numpy as np
import matplotlib.pyplot as plt

def align_signals(x1, n1, x2, n2):

    n_min = min(n1, n2)
    n_max = max(n1 + len(x1) - 1, n2 + len(x2) - 1)
    n = np.arange(n_min, n_max + 1)

    y1 = np.zeros(len(n))
    y2 = np.zeros(len(n))

    y1[(n >= n1) & (n < n1 + len(x1))] = x1
    y2[(n >= n2) & (n < n2 + len(x2))] = x2

    return y1, y2, n

def multiply_signals(x1, n1, x2, n2):

    x, h, n = align_signals(x1, n1, x, n2)
    res = np.zeros(len(x))
    for i in range(len(x)):
      res[i] = x[i]*h[i];
    return res, n

def signal_addition(x1, n1, x2, n2):

    y1, y2, n = align_signals(x1, n1, x2, n2)
    return y1 + y2, n

def signal_shifting(x, n, shift):

    n_shifted = n + shift
    return x, n_shifted

def signal_folding(x, n):

    n_folded = -(n+len(x)-1)
    x_folded = x[::-1]
    return x_folded, n_folded

def conv(x, n1, h, n2):
    n_conv = n1+n2
    l = len(x)+len(h)-1
    y = np.zeros(l)

    h_folded, n2_folded = signal_folding(h, n2)
    for i in range(l):
      h_shifted, n2_shifted = signal_shifting(h_folded, n2_folded, n_conv + i)
      multiplied, n = multiply_signals(x, n1, h_shifted, n2_shifted)
      for a in multiplied:
        y[i]+=a

    return y, np.arange(n_conv, n_conv + l)

x1 = np.array([1, 5, 3, 1, 1])
n1 = -2  # Start index of x1
x2 = np.array([1, 2, 1, 2])
n2 = -1  # Start index of x2

y, n = conv(x1, n1, x2, n2)
print("Convoluted signal is: ", y , "\n")

# Plotting the results
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.stem(np.arange(n1, n1+len(x1)), x1)
plt.title('X')

plt.subplot(3, 1, 2)
plt.stem(np.arange(n2, n2+len(x2)), x2)
plt.title('H')

plt.subplot(3, 1, 3)
plt.stem(n, y)
plt.title('X*H')

plt.tight_layout()
plt.show()