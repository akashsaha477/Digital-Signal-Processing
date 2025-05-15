import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, tf2zpk

zeros, poles, k = tf2zpk([1, 0, 0, 0], [1, -0.9, -0.81, 0.729])

print("Zeros:", zeros)
print("Poles:", poles)

def plot_pole_zero(poles, zeros):
    plt.figure(figsize=(6, 6))
    plt.axhline(0, color='red', lw=0.5)
    plt.axvline(0, color='red', lw=0.5)

    plt.scatter(np.real(zeros), np.imag(zeros), s=50, marker='o', facecolors='none', edgecolors='b', label='Zeros')
    plt.scatter(np.real(poles), np.imag(poles), s=50, marker='x', color='r', label='Poles')

    plt.title('Pole and Zero')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

plot_pole_zero(poles, zeros)