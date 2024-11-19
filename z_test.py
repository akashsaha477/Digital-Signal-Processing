import numpy as np
from scipy.signal import lfilter
import matplotlib.pyplot as plt

num_coefs = [1]
den_coefs = [1, -0.5, 0] 

n = 30  
impulse = np.zeros(n)
impulse[2] = 1 

inverse_z_transform = lfilter(num_coefs, den_coefs, impulse)



plt.stem(np.arange(n), inverse_z_transform)
plt.title('Inverse Z-Transform')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid()
plt.show()