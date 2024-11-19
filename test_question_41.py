import numpy as np
import matplotlib.pyplot as plt
def manual_dft_k(signal, k, N):
    result = 0j
    for n in range(N):
        result += signal[n] * np.exp(-2j * np.pi * k * n / N)
    return result

N = 16
x = np.zeros(N)
x[0:9] = 1

y = np.zeros(N)
y[N-8:N] = 0.5
y[0] = 1.0
y[1:9] = 0.5

X_manual = [manual_dft_k(x, k, N) for k in range(2)]
Y_manual = [manual_dft_k(y, k, N) for k in range(2)]

print("Manual DFT calculation for k=0,1:")
print(f"X[0] = {X_manual[0]:.4f}")
print(f"X[1] = {X_manual[1]:.4f}")

print(f"Y[0] = {Y_manual[0]:.4f}")
print(f"Y[1] = {Y_manual[1]:.4f}")

X = np.fft.fft(x)
Y = np.fft.fft(y)

print("\nNumPy FFT verification for k=0,1:")



print(f"X = {X[0]:.4f}+{X[1]:.4f}")

print(f"Y = {Y[0]:.4f}+{Y[1]:.4f}")


print("\nReal part differences:")
print(f"k=0: {np.abs(np.real(X[0]) - np.real(Y[0])):.10f}")
print(f"k=1: {np.abs(np.real(X[1]) - np.real(Y[1])):.10f}")


abc=Y[0]+Y[1]
print(abc)
xyz=X[0]+X[1]
print(xyz)

print("\nReal part differences:")
print(f"k=0: {np.abs(xyz - abc)}")


plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.stem(np.arange(N), np.abs(X))
plt.title('DFT of X')

plt.subplot(2, 1, 2)
plt.stem(np.arange(N), np.abs(Y))
plt.title('DFT of Y')

plt.tight_layout()
plt.show()
