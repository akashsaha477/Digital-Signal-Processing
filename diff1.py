import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 51)
x = (0.8) ** n
h = (-0.9) ** n

y_analytical = np.zeros(len(n))
for i in range(len(n)):
    for k in range(i + 1):
        if k < len(x) and (i - k) < len(h):
            y_analytical[i] += x[k] * h[i - k]

x_truncated = (0.8) ** np.arange(0, 26)
h_truncated = (-0.9) ** np.arange(0, 26)
y_manual_conv = np.zeros(len(n))
for n_val in range(len(n)):
    sum_value = 0
    for k in range(n_val + 1):
        if k < len(x_truncated) and (n_val - k) < len(h_truncated):
            sum_value += x_truncated[k] * h_truncated[n_val - k]
    y_manual_conv[n_val] = sum_value

y_filter_conv = np.zeros(len(n))
for n_val in range(len(n)):
    sum_value = 0
    for k in range(n_val + 1):
        if k < len(x) and (n_val - k) < len(h):
            sum_value += x[k] * h[n_val - k]
    y_filter_conv[n_val] = sum_value

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.stem(np.arange(0, 51), y_analytical)
plt.title("y[n] from analytical solution")
plt.xlabel('n')
plt.ylabel('y1[n]')

plt.subplot(1, 3, 2)
plt.stem(np.arange(0, 51), y_manual_conv)
plt.title("y[n] from manual convolution (truncated)")
plt.xlabel('n')
plt.ylabel('y2[n]')

plt.subplot(1, 3, 3)
plt.stem(np.arange(0, 51), y_filter_conv)
plt.title("y[n] from manual filter convolution")
plt.xlabel('n')
plt.ylabel('y3[n]')

plt.tight_layout()
plt.show()
