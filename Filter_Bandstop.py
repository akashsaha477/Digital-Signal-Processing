import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import tf2zpk

frequency = np.linspace(-2 * np.pi, 2 * np.pi, 1024)
z_domain = np.exp(1j * frequency)

# Filter parameters
damping = 0.8
resonance = 0.5

transfer_function_numerator = ((1 + damping) / 2) * (1 - 2 * resonance * z_domain**-1 + z_domain**-2)
transfer_function_denominator = 1 - resonance * (1 + damping) * z_domain**-1 + damping * z_domain**-2
frequency_response = transfer_function_numerator / transfer_function_denominator

magnitude_response = np.abs(frequency_response)
phase_response = np.angle(frequency_response)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(frequency, magnitude_response)
plt.title('Magnitude Spectrum of Band Stop Filter')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(frequency, phase_response)
plt.title('Phase Spectrum of Band Stop Filter')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Phase (rad)')
plt.grid(True)

plt.tight_layout()
plt.show()

transfer_function_numerator_coeff = [(1 + damping) / 2, -2 * resonance * (1 + damping) / 2, (1 + damping) / 2] 
transfer_function_denominator_coeff = [1, -resonance * (1 + damping), damping] 

roots_zeros, roots_poles, _ = tf2zpk(transfer_function_numerator_coeff, transfer_function_denominator_coeff)

# Plot pole-zero diagram
plt.figure(figsize=(6, 6))
plt.plot(np.real(roots_zeros), np.imag(roots_zeros), 'go', label='Zeros') 
plt.plot(np.real(roots_poles), np.imag(roots_poles), 'rx', label='Poles')
plt.title('Pole-Zero Plot')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid(True)
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.legend()
plt.show()
