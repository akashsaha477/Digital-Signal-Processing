import numpy as np
import matplotlib.pyplot as plt


X1 = np.array([1, 2, 3, 4])
n1 = np.arange(-1, 3)  


delay = -2
x_n_minus_2 = np.roll(X1, delay)  
n_shifted = n1 + delay  


x_n_minus_2[:delay] = 0  

# Plot 
plt.stem(n1, X1, label='x(n)')
plt.stem(n_shifted, x_n_minus_2, linefmt='r-', markerfmt='ro', basefmt='r-', label='x(n-2)')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Original and Delayed Sequences')
plt.grid()
plt.show()









