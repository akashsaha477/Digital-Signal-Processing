import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

omega0 = np.pi / 4
r_values = [0.85, 0.95]
omega = np.linspace(-2 * np.pi, 2 * np.pi, 1024)

def notch_filter(r, omega0):
    b = np.array([1, -2 * np.cos(omega0), 1])
    a = np.array([1, -2 * r * np.cos(omega0), r**2])
    return b, a

plt.figure(figsize=(12, 8))

for i, r in enumerate(r_values):
    b, a = notch_filter(r, omega0)
    w, h = signal.freqz(b, a, worN=omega)
    
    magnitude = np.abs(h)
    phase = np.angle(h)
    
    plt.subplot(2, 2, i + 1)
    plt.plot(w, 20 * np.log10(magnitude), label=f'r = {r}')
    plt.title(f'Magnitude Spectrum (r = {r})')
    plt.ylabel('Magnitude (dB)')
    plt.xlabel('Frequency (radians/sample)')
    plt.grid()
    plt.legend()
    
    plt.subplot(2, 2, i + 3)
    plt.plot(w, phase, label=f'r = {r}')
    plt.title(f'Phase Spectrum (r = {r})')
    plt.ylabel('Phase (radians)')
    plt.xlabel('Frequency (radians/sample)')
    plt.grid()
    plt.legend()

plt.tight_layout()
plt.show()

b1, a1 = notch_filter(r_values[0], omega0)
b2, a2 = notch_filter(r_values[1], omega0)

_, h1 = signal.freqz(b1, a1, worN=omega)
_, h2 = signal.freqz(b2, a2, worN=omega)

magnitude_diff = np.abs(h1) - np.abs(h2)

plt.figure(figsize=(6, 4))
plt.plot(w, 20 * np.log10(np.abs(magnitude_diff)), label='Magnitude Difference')
plt.title('Magnitude Difference between r = 0.85 and r = 0.95')
plt.ylabel('Difference (dB)')
plt.xlabel('Frequency (radians/sample)')
plt.grid()
plt.legend()
plt.show()
