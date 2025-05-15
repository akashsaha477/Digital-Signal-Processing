import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

def zero_padding(x1, n1, left_limit, right_limit):
    n_min = min(n1, left_limit);
    n_max = max(n1 + len(x1) -1, right_limit);
    n = np.arange(n_min, n_max + 1);

    y = np.zeros(len(n));
    y1[(n >= n1) & (n < n1 + len(x1))] = x1;
    return y,n

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

    x, h, n = align_signals(x1, n1, x2, n2)
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

def analytical_solution(n):
    x = np.zeros(len(n));
    for i in range(len(n)):
        x[i] = (9/17)*((-0.9)**i)*(1 - ((-8/9)**(i+1)));
    return x;1

def truncate_seq(a, n):
    x = np.zeros(n);
    for i in range(n):
        x[i] = (a)**i;
    return x;

num = [1, 0, 0];
den = [1, 0.1, -0.72];
impulse = np.zeros(51);
impulse[0] = 1;

y2 = lfilter(num, den, impulse);

n = np.arange(0, 50);
x1 = analytical_solution(n);
y1, _ = conv(truncate_seq(0.8, 26), 0, truncate_seq(-0.9, 26), 0);
print(y1)

plt.figure(figsize=(8, 6))

plt.subplot(1, 3, 1)
plt.stem(n, x1)
plt.title('Convolution by Analysis')
plt.xlabel('n')
plt.ylabel('y(n)')

plt.subplot(1, 3, 2)
plt.stem(np.arange(0, 51), y1)
plt.title('Convolution by Computation')
plt.xlabel('n')
plt.ylabel('y(n)')

plt.subplot(1, 3, 3)
plt.stem(np.arange(0, 51), y2)
plt.title('Convolution by lfilter')
plt.xlabel('n')
plt.ylabel('y(n)')


plt.tight_layout()
plt.show()