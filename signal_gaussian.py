#    x(n) ={+1, +1, +1, +1,+1,-1 -1, +1,+1 -1,+1 -1, +1}


import numpy as np
import matplotlib.pyplot as plt
import math


def align_signals(seq1, start1, seq2, start2):

    start_min = min(start1, start2)
    start_max = max(start1 + len(seq1) - 1, start2 + len(seq2) - 1)
    n = np.arange(start_min, start_max + 1)

    sig1 = np.zeros(len(n))
    sig2 = np.zeros(len(n))

    sig1[(n >= start1) & (n < start1 + len(seq1))] = seq1
    sig2[(n >= start2) & (n < start2 + len(seq2))] = seq2

    return sig1, sig2, n

 

def multiply_signals(seq1, start1, seq2, start2):

    sig1, sig2, n = align_signals(seq1, start1, seq2, start2)
    res = np.zeros(len(sig1))
    for i in range(len(sig1)):
      res[i] = sig1[i]*sig2[i]
    return res, n




def fold_signal(seq, start):

    n_folded = -(start+len(seq)-1)
    seq_folded = seq[::-1]
    return seq_folded, n_folded





def shift_signal(seq, start, shift):

    n_shifted = start + shift
    return seq, n_shifted


def add_signals(seq1, start1, seq2, start2):

    sig1, sig2, n = align_signals(seq1, start1, seq2, start2)
    return sig1 + sig2, n




def convolve(seq1, start1, seq2, start2):
    n_conv = start1+start2
    l = len(seq1)+len(seq2)-1
    y = np.zeros(l)

    seq2_folded, start2_folded = fold_signal(seq2, start2)
    for i in range(l):
      seq2_shifted, start2_shifted = shift_signal(seq2_folded, start2_folded, n_conv + i)
      multiplied, n = multiply_signals(seq1, start1, seq2_shifted, start2_shifted)
      for a in multiplied:
        y[i]+=a

    return y, np.arange(n_conv, n_conv + l)

def correlate(seq1, start1, seq2, start2):
    seq2_folded, start2_folded = fold_signal(seq2, start2)
    y, n = convolve(seq1, start1, seq2_folded, start2_folded);
    return y, n;


t = np.linspace(0, 99, 500)
def gaussian(m, v, t):
  return (1/math.sqrt(2*np.pi*v))*(np.exp(-((t-m)*(t-m))/(2*v)))

v = gaussian(0, 0.01, t)
x = np.array([1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1])
x1, n1 = shift_signal(0.9*x, 0, 20);
res, n = add_signals(x1, n1, v, 0);
final, n_final = correlate(res, -20, v, 0)

plt.figure(figsize=(10, 8))
plt.subplot(4, 1, 1)
plt.stem(np.arange(0, 0+len(x1)), x1)
plt.title('Barker sequence')
plt.xlabel('n')
plt.ylabel('x(n)')

plt.subplot(4, 1, 2)
plt.stem(t, v, '-r')
plt.title('Gaussian noise')
plt.xlabel('t')
plt.ylabel('v(t)')

plt.subplot(4, 1, 3)
plt.stem(n, res, '-g')
plt.xlim(0, 100)
plt.title('y(n)')
plt.xlabel('n')
plt.ylabel('ax(n-D) + v(n)')
# a = 0.9, D = 20

plt.subplot(4, 1, 4)
plt.stem(n_final, final, '-b')
plt.xlim(-100, 12)
plt.title('Distance measurement in radar from correlation')
plt.xlabel('n')

plt.tight_layout()
plt.show()