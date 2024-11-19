import numpy as np
import matplotlib.pyplot as plt

w0 = 2 * np.pi * 10**6
T0 = 2 * np.pi / w0

#Unit impulse function
t0 = np.linspace(-4 * T0, 4 * T0, num=100)
len_t0 = len(t0)
unit_impulse0 = np.zeros(len_t0)
unit_impulse0[np.argmin(np.abs(t0))] = 1

#Unit step function
unit_step0 = np.heaviside(t0, 1)

#Unit ramp function
unit_ramp0 = np.zeros(len_t0)
for i, l in enumerate(t0):
    if l < 0:
        unit_ramp0[i] = 0
    elif l >= 0:
        unit_ramp0[i] = l

#Unit exponential
unit_exp0 = np.zeros(len_t0)
for i, l in enumerate(t0):
    if l < 0:
        unit_exp0[i] = 0
    elif l >= 0:
        unit_exp0[i] = np.exp(l)


unit_impulse_mod0 = unit_impulse0 * np.sin(w0 * t0)
unit_step_mod0 = unit_step0 * np.sin(w0 * t0)
unit_ramp_mod0 = unit_ramp0 * np.sin(w0 * t0)
unit_exp_mod0 = unit_exp0 * np.sin(w0 * t0)

# Plot
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plt.plot(t0, unit_impulse_mod0)
plt.title('Unit Impulse Function')

plt.subplot(2, 2, 2)
plt.plot(t0, unit_step_mod0)
plt.title('Unit Step Function')

plt.subplot(2, 2, 3)
plt.plot(t0, unit_ramp_mod0)
plt.title('Unit Ramp Function')

plt.subplot(2, 2, 4)
plt.plot(t0, unit_exp_mod0)
plt.title('Unit Exponential Function')
plt.show()

