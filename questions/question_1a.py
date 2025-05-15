import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 1e-6  # Time period
omega = 2 * np.pi * 10**6
t = np.linspace(-4 * T, 4 * T, 1000)

# Signals
unit_impulse = np.where(np.abs(t) < 1e-9, 1, 0)  # Approximation of impulse at t=0
unit_step = np.where(t >= 0, 1, 0)
unit_ramp = np.where(t >= 0, t, 0)
exponential_signal = np.exp(-omega * t)

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.stem(t, unit_impulse, basefmt=" ")
plt.title('Unit Impulse Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 2, 2)
plt.plot(t, unit_step)
plt.title('Unit Step Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 2, 3)
plt.plot(t, unit_ramp)
plt.title('Unit Ramp Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 2, 4)
plt.plot(t, exponential_signal)
plt.title('Exponential Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
