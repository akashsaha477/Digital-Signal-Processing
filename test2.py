import numpy as np
import matplotlib.pyplot as plt


n=int(input("Enter the amplitude:"))


amplitude = n
time = np.arange(-10, 11, 1) 


unit_pulse = np.array([amplitude if t == 0 else 0 for t in time])

unit_impulse = np.array([amplitude if t == 0 else 0 for t in time])

unit_ramp = np.array([amplitude * t if t >= 0 else 0 for t in time])


unit_exponential = np.array([amplitude * np.exp(t) if t >= 0 else 0 for t in time])


plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.stem(time, unit_pulse)
plt.title('Unit Pulse')

plt.subplot(2, 2, 2)
plt.stem(time, unit_impulse)
plt.title('Unit Impulse')

plt.subplot(2, 2, 3)
plt.stem(time, unit_ramp)
plt.title('Unit Ramp')

plt.subplot(2, 2, 4)
plt.stem(time, unit_exponential)
plt.title('Unit Exponential')

plt.tight_layout()
plt.show()


def add_signals(signal1, signal2):
    return signal1 + signal2

def subtract_signals(signal1, signal2):
    return signal1 - signal2

def multiply_signals(signal1, signal2):
    return signal1 * signal2

def fold_signal(signal):
    return signal[::-1]

def shift_signal(signal, shift):
    shifted_signal = np.zeros_like(signal)
    if shift > 0:
        shifted_signal[shift:] = signal[:-shift]
    else:
        shifted_signal[:shift] = signal[-shift:]
    return shifted_signal


shift = 3  


added_signal = add_signals(unit_pulse, unit_ramp)
subtracted_signal = subtract_signals(unit_pulse, unit_ramp)
multiplied_signal = multiply_signals(unit_pulse, unit_ramp)
folded_signal = fold_signal(unit_pulse)
shifted_signal = shift_signal(unit_pulse, shift)


plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.stem(time, added_signal)
plt.title('Added Signal')

plt.subplot(3, 2, 2)
plt.stem(time, subtracted_signal)
plt.title('Subtracted Signal')

plt.subplot(3, 2, 3)
plt.stem(time, multiplied_signal)
plt.title('Multiplied Signal')

plt.subplot(3, 2, 4)
plt.stem(time, folded_signal)
plt.title('Folded Signal')

plt.subplot(3, 2, 5)
plt.stem(time, shifted_signal, )
plt.title('Shifted Signal')

plt.tight_layout()
plt.show()
