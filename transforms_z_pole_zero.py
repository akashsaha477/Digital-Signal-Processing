import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal

poles = [0.4]
zeros = []
plt.plot(np.real(poles), np.imag(poles), 'x', label='Poles')
plt.plot(np.real(zeros), np.imag(zeros), 'o', label='Zeros')
plt.legend()
plt.xlabel('Real axis')
plt.ylabel('Imaginary axis')
plt.title('Pole-Zero Plot')
plt.show()
plt.grid(True)
plt.axis('equal')