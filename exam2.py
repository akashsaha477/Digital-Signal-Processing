import numpy as np
import matplotlib.pyplot as plt

poles = [0.4]
zeros = []

theta = np.linspace(0, 2 * np.pi, 1000)
unit_circle = np.exp(1j * theta)

plt.figure(figsize=(6, 6))
plt.plot(np.real(unit_circle), np.imag(unit_circle), 'b--')

if zeros:
    plt.scatter(np.real(zeros), np.imag(zeros), color='b', marker='o', label='Zeros')

plt.scatter(np.real(poles), np.imag(poles), color='r', marker='x', label='Poles')

plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.title('Pole-Zero Plot')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.legend()
plt.grid(True)
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])

plt.show()

