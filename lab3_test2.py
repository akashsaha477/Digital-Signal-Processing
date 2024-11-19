import numpy as np

#  time reversal
def time_reversal(x, n):
    return x[::-1], -n[::-1]

#  shifting
def time_shift(x, n, k):
    return x, n + k


x_n1 = np.array([1, 2, 3, 4])
n1 = np.arange(-1, 3)  


x_reversed, n_reversed = time_reversal(x_n1, n1)


x_shifted, n_shifted = time_shift(x_reversed, n_reversed, 2)

print("Original sequence x(n1):", x_n1)
print("Original indices n1:", n1)
print("Time-reversed sequence x(-n1):", x_reversed)
print("Time-reversed indices -n1:", n_reversed)
print("Shifted sequence x(-n + 2):", x_shifted)
print("Shifted indices -n1 + 2:", n_shifted)
