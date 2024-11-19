import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import tf2zpk

alpha = 0.8
beta = 0.34
w = np.linspace(-2 * np.pi, 2 * np.pi, 1024)
z = np.exp(1j * w)

numerator = (1 - alpha) / 2 * (1 - z**-2)
denominator = 1 - beta * (1 + alpha) * z**-1 + alpha * z**-2
H_BP = numerator / denominator

magnitude = np.abs(H_BP)
phase = np.angle(H_BP)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(w, magnitude)
plt.title('Mag Spec of BPF')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(w, phase)
plt.title('Phase Spec of BPF')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Phase (rad)')
plt.grid(True)

plt.tight_layout()
plt.show()

num_coeff = [(1 - alpha) / 2, 0, -(1 - alpha) / 2]
den_coeff = [1, -beta * (1 + alpha), alpha] 

zeros, poles, _ = tf2zpk(num_coeff, den_coeff)

plt.figure(figsize=(6, 6))
plt.plot(np.real(zeros), np.imag(zeros), 'go', label='Zeros') 
plt.plot(np.real(poles), np.imag(poles), 'rx', label='Poles')  
plt.title('Pole-Zero Plot')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid(True)
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.legend()
plt.show()