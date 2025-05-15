import numpy as np
from scipy.signal import lfilter
import matplotlib.pyplot as plt

num_coefs = [39.0625]
den_coefs = [1, -0.4] 


def x_n(n1):
    return 0.4**(n1-4) * (n1 >= 0)

n1 = np.arange(0, 21)
x_values = x_n(n1)


n2 = 30  
impulse = np.zeros(n2)
impulse[0] = 1 

inverse_z_transform = lfilter(num_coefs, den_coefs, impulse)


plt.subplot(2, 1, 1)
plt.stem(n1, x_values, basefmt=" ")
plt.title('Sequence x(n) = 0.4^(n-4) * u(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(np.arange(n2), inverse_z_transform)
plt.title('Inverse Z-Transform')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid()
plt.show()














