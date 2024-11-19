import numpy as np
import matplotlib.pyplot as plt

T_sin = 1/3  
T_cos = 1/5  

#time axis for signals
t_discrete_sin = np.linspace(0, 5*T_sin, 500)
t_discrete_cos = np.linspace(0, 5*T_cos, 500)
t_discrete_other = np.linspace(0, 5, 500)


sin_signal_discrete = np.sin(2 * np.pi * 3 * t_discrete_sin)
cos_signal_discrete = np.cos(2 * np.pi * 5 * t_discrete_cos)
step_signal_discrete = np.heaviside(t_discrete_other, 1)
impulse_signal_discrete = np.where(t_discrete_other == 0, 1, 0)
ramp_signal_discrete = t_discrete_other

# Plot 
plt.figure(figsize=(15, 10))

plt.subplot(5, 1, 1)
plt.stem(t_discrete_sin, sin_signal_discrete)
plt.title('Discrete sin(2π3t)')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')

plt.subplot(5, 1, 2)
plt.stem(t_discrete_cos, cos_signal_discrete)
plt.title('Discrete cos(2π5t)')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')

plt.subplot(5, 1, 3)
plt.stem(t_discrete_other, step_signal_discrete)
plt.title('Discrete Step Signal')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')

plt.subplot(5, 1, 4)
plt.stem(t_discrete_other, impulse_signal_discrete)
plt.title('Discrete Impulse Signal')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')

plt.subplot(5, 1, 5)
plt.stem(t_discrete_other, ramp_signal_discrete)
plt.title('Discrete Ramp Signal')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
