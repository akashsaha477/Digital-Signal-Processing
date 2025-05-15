import numpy as np
import matplotlib.pyplot as plt


def pad_sequences(seq1, seq2):
    max_len = max(len(seq1), len(seq2))
    seq1 = np.pad(seq1, (0, max_len - len(seq1)), 'constant')
    seq2 = np.pad(seq2, (0, max_len - len(seq2)), 'constant')
    return seq1, seq2


def fold_signal(seq):
    return seq[::-1]


def circular_shift(seq, shift):
    return np.roll(seq, shift)


def circular_convolve(seq1, seq2):
   
    seq1, seq2 = pad_sequences(seq1, seq2)
    N = len(seq1)
    result = np.zeros(N)
    
    
    folded_seq2 = fold_signal(seq2)
    
    
    for n in range(N):
        
        shifted_seq2 = circular_shift(folded_seq2, n)
       
        result[n] = np.sum(seq1 * shifted_seq2)

    return result

def circular_convolve_dft(seq1, seq2):
    seq1, seq2 = pad_sequences(seq1, seq2)
    dft_seq1 = np.fft.fft(seq1)
    dft_seq2 = np.fft.fft(seq2)
    result_dft = np.fft.ifft(dft_seq1 * dft_seq2)
    return np.real(result_dft)


seq1 = np.array([1, 2, 3, 4])
seq2 = np.array([1, 2, 2])


circular_result = circular_convolve(seq1, seq2)


dft_result = circular_convolve_dft(seq1, seq2)

print("Circular Convolution (manual):", circular_result)
print("Circular Convolution (DFT verification):", dft_result)


plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.stem(seq1)
plt.title('Sequence x1[n]')

plt.subplot(3, 1, 2)
plt.stem(seq2)
plt.title('Sequence x2[n]')

plt.subplot(3, 1, 3)
plt.stem(circular_result)
plt.title('Circular Convolution Result')

plt.tight_layout()
plt.show()