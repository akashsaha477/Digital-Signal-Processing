import numpy as np
import matplotlib.pyplot as plt


given_sequence_1 = np.arange(-2, 3)
x_1 = np.array([1, 2, 0, 3, 4])

given_sequence_2 = np.arange(-1, 5)
x_2 = np.array([2, 0, 3, 4, 5, 6])


combined_range = np.arange(min(given_sequence_1[0], given_sequence_2[0]),
                           max(given_sequence_1[-1], given_sequence_2[-1]) + 1)


x_1_padded = np.zeros(len(combined_range))
x_2_padded = np.zeros(len(combined_range))

x_1_padded[np.in1d(combined_range, given_sequence_1)] = x_1
x_2_padded[np.in1d(combined_range, given_sequence_2)] = x_2


x_1_plus_x_2 = x_1_padded + x_2_padded
x_1_minus_x_2 = x_1_padded - x_2_padded
x_1_times_x_2 = x_1_padded * x_2_padded


plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(combined_range, x_1_plus_x_2)
plt.title('X1 + X2')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(combined_range, x_1_minus_x_2)
plt.title('X1 - X2')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(combined_range, x_1_times_x_2)
plt.title('X1 * X2')
plt.grid(True)

plt.tight_layout()
plt.show()


x_1_neg_n1 = x_1_padded[::-1]
x_2_neg_n2 = x_2_padded[::-1]

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.stem(-combined_range, x_1_neg_n1)
plt.title('X1(-n1)')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(-combined_range, x_2_neg_n2)
plt.title('X2(-n2)')
plt.grid(True)

plt.tight_layout()
plt.show()


n_shifted_plus = combined_range + 2
n_shifted_minus = combined_range - 2


x_1_shifted_plus = np.roll(x_1_padded, 2)
x_1_shifted_minus = np.roll(x_1_padded, -2)

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.stem(combined_range, x_1_shifted_plus)
plt.title('X1(n1 + 2)')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(combined_range, x_1_shifted_minus)
plt.title('X1(n1 - 2)')
plt.grid(True)

plt.tight_layout()
plt.show()
