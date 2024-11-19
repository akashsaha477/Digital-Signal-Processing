import numpy as np
import matplotlib.pyplot as plt

alpha = 0.9
num_samples = 1024

w = np.linspace(-np.pi, np.pi, num_samples)

numerator = (1 - alpha) / 2 * (1 + np.exp(-1j * w))
denominator = (1 - alpha * np.exp(-1j * w))
H_w = numerator / denominator

magnitude_response = np.abs(H_w)
phase_response = np.angle(H_w)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(w, magnitude_response)
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(w, phase_response)
plt.title('Phase Spectrum')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Phase (radians)')
plt.grid(True)

plt.tight_layout()
plt.show()


from numpy import roots

numerator_coeffs = [(1 - alpha) / 2, (1 - alpha) / 2]
denominator_coeffs = [1, -alpha]

zeros = roots(numerator_coeffs)
poles = roots(denominator_coeffs)

plt.figure(figsize=(6, 6))

unit_circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
plt.gca().add_artist(unit_circle)

plt.scatter(np.real(zeros), np.imag(zeros), color='blue', label='Zeros', marker='o', s=100)
plt.scatter(np.real(poles), np.imag(poles), color='red', label='Poles', marker='x', s=100)

plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.title('Poles and Zeros')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid(True)
plt.legend()

plt.show()
