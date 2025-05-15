import numpy as np
import matplotlib.pyplot as plt

# Signal 1
time_1 = np.arange(-2, 3)
signal_1 = np.array([1, 2, 0, 3, 4])

# Signal 2
time_2 = np.arange(-1, 5)
signal_2 = np.array([2, 0, 3, 4, 5, 6])

# User-defined functions for operations
def add_signals(signal_1, time_1, signal_2, time_2):
    time = np.arange(min(min(time_1), min(time_2)), max(max(time_1), max(time_2)) + 1)
    extended_signal_1 = np.zeros_like(time)
    extended_signal_2 = np.zeros_like(time)
    
    for i in range(len(time)):
        if time[i] in time_1:
            extended_signal_1[i] = signal_1[np.where(time_1 == time[i])[0][0]]
        if time[i] in time_2:
            extended_signal_2[i] = signal_2[np.where(time_2 == time[i])[0][0]]
    
    return extended_signal_1 + extended_signal_2, time

def subtract_signals(signal_1, time_1, signal_2, time_2):
    time = np.arange(min(min(time_1), min(time_2)), max(max(time_1), max(time_2)) + 1)
    extended_signal_1 = np.zeros_like(time)
    extended_signal_2 = np.zeros_like(time)
    
    for i in range(len(time)):
        if time[i] in time_1:
            extended_signal_1[i] = signal_1[np.where(time_1 == time[i])[0][0]]
        if time[i] in time_2:
            extended_signal_2[i] = signal_2[np.where(time_2 == time[i])[0][0]]
    
    return extended_signal_1 - extended_signal_2, time

def multiply_signals(signal_1, time_1, signal_2, time_2):
    time = np.arange(min(min(time_1), min(time_2)), max(max(time_1), max(time_2)) + 1)
    extended_signal_1 = np.zeros_like(time)
    extended_signal_2 = np.zeros_like(time)
    
    for i in range(len(time)):
        if time[i] in time_1:
            extended_signal_1[i] = signal_1[np.where(time_1 == time[i])[0][0]]
        if time[i] in time_2:
            extended_signal_2[i] = signal_2[np.where(time_2 == time[i])[0][0]]
    
    return extended_signal_1 * extended_signal_2, time

def time_reverse(signal, time):
    return signal[::-1], -time[::-1]

def time_shift(signal, time, shift):
    return signal, time + shift

# Built-in functions for operations using NumPy
def built_in_add(signal_1, time_1, signal_2, time_2):
    return np.add(signal_1, signal_2), time_1  # Assuming the lengths are equal for simplicity

def built_in_subtract(signal_1, time_1, signal_2, time_2):
    return np.subtract(signal_1, signal_2), time_1  # Assuming the lengths are equal for simplicity

def built_in_multiply(signal_1, time_1, signal_2, time_2):
    return np.multiply(signal_1, signal_2), time_1  # Assuming the lengths are equal for simplicity

# Performing operations using user-defined functions
signal_add, time_add = add_signals(signal_1, time_1, signal_2, time_2)
signal_subtract, time_subtract = subtract_signals(signal_1, time_1, signal_2, time_2)
signal_multiply, time_multiply = multiply_signals(signal_1, time_1, signal_2, time_2)
signal_reverse_1, time_reverse_1 = time_reverse(signal_1, time_1)
signal_reverse_2, time_reverse_2 = time_reverse(signal_2, time_2)
signal_shifted_right, time_shifted_right = time_shift(signal_1, time_1, 2)
signal_shifted_left, time_shifted_left = time_shift(signal_1, time_1, -2)

# Plotting the results
plt.figure(figsize=(12, 12))

plt.subplot(3, 2, 1)
plt.stem(time_add, signal_add, basefmt=" ")
plt.title('Signal 1 + Signal 2')

plt.subplot(3, 2, 2)
plt.stem(time_subtract, signal_subtract, basefmt=" ")
plt.title('Signal 1 - Signal 2')

plt.subplot(3, 2, 3)
plt.stem(time_multiply, signal_multiply, basefmt=" ")
plt.title('Signal 1 * Signal 2')

plt.subplot(3, 2, 4)
plt.stem(time_reverse_1, signal_reverse_1, basefmt=" ")
plt.title('Signal 1(-time_1)')

plt.subplot(3, 2, 5)
plt.stem(time_reverse_2, signal_reverse_2, basefmt=" ")
plt.title('Signal 2(-time_2)')

plt.subplot(3, 2, 6)
plt.stem(time_shifted_right, signal_shifted_right, basefmt=" ", label='Signal 1(time_1+2)')
plt.stem(time_shifted_left, signal_shifted_left, basefmt=" ", linefmt='r--', markerfmt='ro', label='Signal 1(time_1-2)')
plt.legend()
plt.title('Signal 1 Time Shifted')

plt.tight_layout()
plt.show()

# Compare with built-in functions
signal_add_built_in, time_add_built_in = built_in_add(signal_1, time_1, signal_2, time_2)
signal_subtract_built_in, time_subtract_built_in = built_in_subtract(signal_1, time_1, signal_2, time_2)
signal_multiply_built_in, time_multiply_built_in = built_in_multiply(signal_1, time_1, signal_2, time_2)

# Print comparison
print(f'Addition - User-defined: {signal_add}, Built-in: {signal_add_built_in}')
print(f'Subtraction - User-defined: {signal_subtract}, Built-in: {signal_subtract_built_in}')
print(f'Multiplication - User-defined: {signal_multiply}, Built-in: {signal_multiply_built_in}')

