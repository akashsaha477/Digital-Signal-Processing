import numpy as np


sequence = np.array([1, 2, 3, 4])
fft_result = np.fft.fft(sequence)

length = len(sequence)
dft_result = np.zeros(length, dtype=complex)

for k in range(length):
    for n in range(length):
        dft_result[k] += sequence[n] * np.exp(-2j * np.pi * k * n / length)




print("DFT (manual calculation):", dft_result)
print("DFT (using fft ):", fft_result)