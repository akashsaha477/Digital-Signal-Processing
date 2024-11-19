import numpy as np
import matplotlib.pyplot as plt


x = [1, 5, 3, 1, 1]
n1 = np.arange(-2, 3)

h = [1, 2, 1, 2]
n2 = np.arange(-1, 3)


Nx = len(x)
Nh = len(h)
Ny = Nx + Nh - 1


y = [0] * Ny

for n in range(Ny):
    for k in range(Nx):
        if n - k >= 0 and n - k < Nh:
            y[n] += x[k] * h[n - k]


nx = np.arange(0, Nx)
nh = np.arange(0, Nh)
ny = np.arange(min(nx) + min(nh), max(nx) + max(nh) + 1)


plt.stem(ny, y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Convolution Result')
plt.grid(True)
plt.show()




# Display the convolution result in matrix form
print("The convolution result y(n) is:", y)
print("The indices of y(n) are:", ny.tolist())



x = np.array([1, 5, 3, 1, 1])
n_x = np.arange(-1, 3)  

h = np.array([1, 2, 1, 2])
n_h = np.arange(-2, 2)  


def builtin_convolution(x, h):
   
    y = np.convolve(x, h, mode='full')
    n_y = np.arange(-len(y) + 1, len(y))
    return y, n_y

y_builtin, n_y_builtin = builtin_convolution(x, h)



print("Built-in Convolution y(n):", y_builtin)
print("Built-in Convolution n:", n_y_builtin)

