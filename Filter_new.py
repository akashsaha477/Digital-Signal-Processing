import numpy as np
import matplotlib.pyplot as plt

Fs = 2000  
f = np.array([0, 200, 1000])  
n = np.arange(0, 1024)  

omega = 2 * np.pi * f / Fs

x1 = np.cos(omega[1] * n)
x2 = np.cos(omega[2] * n)
x3 = np.cos(omega[0] * n)  
x = x1 + x2 + x3

X = np.fft.fft(x)

frequencies = np.fft.fftfreq(n.size, d=1/Fs)

alpha = 0.9
Hz_lp1 = (1 - alpha**2) / (1 + np.exp(-1j*2*np.pi*frequencies/Fs) - alpha * np.exp(-1j*2*np.pi*frequencies/Fs))

Hz_hp1 = (1 - alpha**2) / (1 - np.exp(-1j*2*np.pi*frequencies/Fs) - alpha * np.exp(-1j*2*np.pi*frequencies/Fs))

K = 0.25
a, b = 0.5, 0.5
Hz_lp2 = K * ((1 + np.exp(-1j*2*np.pi*frequencies/Fs))**2) / ((1 - a*np.exp(-1j*2*np.pi*frequencies/Fs)) * (1 - b*np.exp(-1j*2*np.pi*frequencies/Fs)))

Hz_hp2 = K * ((1 - np.exp(-1j*2*np.pi*frequencies/Fs))**2) / ((1 - a*np.exp(-1j*2*np.pi*frequencies/Fs)) * (1 - b*np.exp(-1j*2*np.pi*frequencies/Fs)))

Y_lp1 = Hz_lp1 * X
Y_hp1 = Hz_hp1 * X
Y_lp2 = Hz_lp2 * X
Y_hp2 = Hz_hp2 * X

y_lp1 = np.fft.ifft(Y_lp1)
y_hp1 = np.fft.ifft(Y_hp1)
y_lp2 = np.fft.ifft(Y_lp2)
y_hp2 = np.fft.ifft(Y_hp2)

plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(n, np.real(y_lp1))
plt.title('Time Domain Output - First Order Low Pass Filter')
plt.xlabel('n')
plt.ylabel('y(n)')

plt.subplot(2, 2, 2)
plt.plot(n, np.real(y_hp1))
plt.title('Time Domain Output - First Order High Pass Filter')
plt.xlabel('n')
plt.ylabel('y(n)')

plt.subplot(2, 2, 3)
plt.plot(n, np.real(y_lp2))
plt.title('Time Domain Output - Second Order Low Pass Filter')
plt.xlabel('n')
plt.ylabel('y(n)')

plt.subplot(2, 2, 4)
plt.plot(n, np.real(y_hp2))
plt.title('Time Domain Output - Second Order High Pass Filter')
plt.xlabel('n')
plt.ylabel('y(n)')

plt.tight_layout()
plt.show()

Y_lp1_fft = np.fft.fft(y_lp1)
Y_hp1_fft = np.fft.fft(y_hp1)
Y_lp2_fft = np.fft.fft(y_lp2)
Y_hp2_fft = np.fft.fft(y_hp2)

plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(frequencies[:512], np.abs(Y_lp1_fft[:512]))
plt.title('Frequency Spectrum - First Order Low Pass Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('|Y(ω)|')

plt.subplot(2, 2, 2)
plt.plot(frequencies[:512], np.abs(Y_hp1_fft[:512]))
plt.title('Frequency Spectrum - First Order High Pass Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('|Y(ω)|')

plt.subplot(2, 2, 3)
plt.plot(frequencies[:512], np.abs(Y_lp2_fft[:512]))
plt.title('Frequency Spectrum - Second Order Low Pass Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('|Y(ω)|')

plt.subplot(2, 2, 4)
plt.plot(frequencies[:512], np.abs(Y_hp2_fft[:512]))
plt.title('Frequency Spectrum - Second Order High Pass Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('|Y(ω)|')

plt.tight_layout()
plt.show()
