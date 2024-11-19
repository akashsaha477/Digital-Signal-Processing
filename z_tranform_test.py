import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter


def plot_pole_zero(poles, zeros):
    plt.figure(figsize=(6, 6))
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)

    plt.scatter(np.real(zeros), np.imag(zeros), s=50, marker='o', facecolors='none', edgecolors='b', label='Zeros')
    plt.scatter(np.real(poles), np.imag(poles), s=50, marker='x', color='r', label='Poles')

    plt.title('Pole-Zero Plot')
    plt.xlabel('Real Part')
    plt.ylabel('Imaginary Part')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

plot_pole_zero([0, 0.5], [0])

