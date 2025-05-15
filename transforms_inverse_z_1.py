import numpy as np
import math
import matplotlib.pyplot as plt

def x_of_n(n):
  if(n<0):
    return 0;
  elif(n == 0):
    return 1;
  else:
    return 0.25*(-0.9)**n + 0.75*(0.9)**n + 0.45*n*(0.9)**(n-1);

def discreteSignal (len, f_of_x, st_ind):
  y = np.zeros(len);
  n = np.arange(st_ind, st_ind + len);
  for i in range(len):
    y[i] = f_of_x(st_ind + i);
  return y, n;

x, n = discreteSignal(8, x_of_n, 0);

print(x)

plt.figure(figsize=(8, 6))

plt.stem(n, x);
plt.title('Signal')
plt.xlabel('n')
plt.ylabel('x(n)')

plt.show()