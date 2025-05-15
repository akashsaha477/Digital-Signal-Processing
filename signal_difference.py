import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Coefficients of the difference equation
# y(n) - y(n-1) + 0.9y(n-2) = x(n)
a = [1, -1, 0.9]  # Denominator coefficients
b = [1]           # Numerator coefficients 

# Time vector
n = np.arange(-20, 101)

# Impulse response 
system = (b, a, 1)
_, h_impulse = signal.dimpulse(system, n=121)  
h_impulse = np.squeeze(h_impulse)

# Step response
_, h_step = signal.dstep(system, n=121) 
h_step = np.squeeze(h_step)

# Time vector
time_vec = np.arange(0, len(h_impulse))

# Plot Impulse 
plt.subplot(2, 1, 1)
plt.stem(time_vec - 20, h_impulse) 
plt.title("Impulse Response")
plt.xlabel('n')
plt.ylabel('h(n)')

# Plot Step 
plt.subplot(2, 1, 2)
plt.stem(time_vec - 20, h_step) 
plt.title("Step Response")
plt.xlabel('n')
plt.ylabel('s(n)')

plt.tight_layout()
plt.show()