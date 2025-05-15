import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

r = 0.9
omega0 = np.pi / 4
omega = np.linspace(-2 * np.pi, 2 * np.pi, 1024)

b = np.array([r**2, -2 * r * np.cos(omega0), 1])
a = np.array([1, -2 * r * np.cos(omega0), r**2])

w, h = signal.freqz(b, a, worN=omega)

magnitude = np.abs(h)
phase = np.angle(h)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(w, 20 * np.log10(magnitude), 'b')
plt.title('Magnitude Spectrum')
plt.ylabel('Magnitude (dB)')
plt.xlabel('Frequency (radians/sample)')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(w, phase, 'r')
plt.title('Phase Spectrum')
plt.ylabel('Phase (radians)')
plt.xlabel('Frequency (radians/sample)')
plt.grid()

plt.tight_layout()
plt.show()
