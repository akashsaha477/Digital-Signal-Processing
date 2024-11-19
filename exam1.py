import numpy as np
import matplotlib.pyplot as plt



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

def convolve1(seq1, start1, seq2, start2):
    #seq2_folded, start2_folded = fold_signal(seq2, start2)
    y, n = convolve(seq1, start1, seq2, start2);
    return y, n;




seq1 = np.array([2, 3, 1, 0, 2, 1])
start1 = -2  
seq2 = np.array([1, 2, 1, 3, 2])
start2 = -2  



y, n = convolve1(seq1, start1, seq2, start2)
print("Convolve signal is: ", y , "\n")

# Plot
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.stem(np.arange(start1, start1+len(seq1)), seq1)
plt.title('X')

plt.subplot(3, 1, 2)
plt.stem(np.arange(start2, start2+len(seq2)), seq2)
plt.title('H')

plt.subplot(3, 1, 3)
plt.stem(n, y)
plt.title('X*H')

plt.tight_layout()
plt.show()


