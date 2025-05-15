import numpy as np

N = 16

x = np.zeros(N)
x[0:9] = 1

y = np.zeros(N)
y[0] = 1
y[1:9] = 0.5
y[-8:] = 0.5

X = np.fft.fft(x)
Y = np.fft.fft(y)

real_X = np.real(X)
real_Y = np.real(Y)

print("Real part of DFT of x[n]:", real_X)
print("Real part of DFT of y[n]:", real_Y)

if np.allclose(real_X, real_Y):
    print("The real parts of the DFTs of x[n] and y[n] are equal.")
else:
    print("The real parts of the DFTs of x[n] and y[n] are NOT equal.")
