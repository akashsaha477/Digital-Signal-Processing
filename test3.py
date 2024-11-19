import numpy as np
import matplotlib.pyplot as plt

X1 = np.array([1, 2, 0, 3, 4])
X2 = np.array([2,0,3,4,5,6])
#n1=-2:2
#n2=-3:3

dt = 1
t1 = np.arange(0,len(X1))*dt
t2 = np.arange(0,len(X2))*dt

discrete_signal_1 = np.zeros(len(X1))
discrete_signal_2 = np.zeros(len(X2))

for i in range(len(X1)):
    discrete_signal_1[i] = X1[i] * np.sin(2*np.pi*t1[i])
    
for j in range(len(X2)):
    discrete_signal_2[j] = X2[j] * np.sin(2*np.pi*t2[j])
    
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.stem(t1, discrete_signal_1)
plt.title('Discrete Signal 1')

plt.subplot(2, 1, 2)
plt.stem(t2, discrete_signal_2)
plt.title('Discrete Signal 2')

plt.tight_layout()
plt.show()

print(X1, "\n")
print(X2, "\n")





added_signal = discrete_signal_1 + discrete_signal_2
subtracted_signal = discrete_signal_1 - discrete_signal_2
multiplied_signal = discrete_signal_1 * discrete_signal_2

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(t1, discrete_signal_1)
plt.title('Discrete Signal 1')

plt.subplot(3, 1, 2)
plt.stem(t2, discrete_signal_2)
plt.title('Discrete Signal 2')

plt.subplot(3, 1, 3)
plt.stem(t1, added_signal)
plt.title('Added Signal')

plt.tight_layout()
plt.show()



'''plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(t1, discrete_signal_1)
plt.title('Discrete Signal 1')

plt.subplot(3, 1, 2)
plt.stem(t2, discrete_signal_2)
plt.title('Discrete Signal 2')

plt.subplot(3, 1, 3)
plt.stem(t1, subtracted_signal)
plt.title('Subtracted Signal')

plt.tight_layout()
plt.show()



plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(t1, discrete_signal_1)
plt.title('Discrete Signal 1')

plt.subplot(3, 1, 2)
plt.stem(t2, discrete_signal_2)
plt.title('Discrete Signal 2')

plt.subplot(3, 1, 3)
plt.stem(t1, multiplied_signal)
plt.title('Multiplied Signal')

plt.tight_layout()
plt.show()
'''
