import numpy as np
import matplotlib.pyplot as plt

def x_n(n):
    return 0.4**(n-4) * (n >= 0)

n = np.arange(0, 21)
x_values = x_n(n)



plt.stem(n, x_values, basefmt=" ")
plt.title('Sequence x(n) = 0.4^(n-4) * u(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.show()

print(x_values)

