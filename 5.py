import numpy as np
import matplotlib.pyplot as plt

# time axis
t_continuous = np.arange(0, 1.01, 0.01)


sin_signal = np.sin(2 * np.pi * 3 * t_continuous)
cos_signal = np.cos(2 * np.pi * 5 * t_continuous)
step_signal = np.heaviside(t_continuous, 1)
impulse_signal = np.where(t_continuous == 0, 1, 0)
ramp_signal = t_continuous

# signals
plt.figure(figsize=(15, 10))

plt.subplot(5, 1, 1)
plt.plot(t_continuous, sin_signal)
plt.title('sin(2π3t)')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')

plt.subplot(5, 1, 2)
plt.plot(t_continuous, cos_signal)
plt.title('cos(2π5t)')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')

plt.subplot(5, 1, 3)
plt.plot(t_continuous, step_signal)
plt.title('Step Signal')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')

plt.subplot(5, 1, 4)
plt.stem(t_continuous, impulse_signal)
plt.title('Impulse Signal')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')

plt.subplot(5, 1, 5)
plt.plot(t_continuous, ramp_signal)
plt.title('ramp Signal')
plt.xlabel('Time (t)')
plt.ylabel('amplitude')

plt.tight_layout()
plt.show()
