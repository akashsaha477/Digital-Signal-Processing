import numpy as np
import matplotlib.pyplot as plt

def ideal_impulse_response(n):
    hd = np.zeros_like(n, dtype=float)
    for i in range(len(n)):
        if n[i] == 0:
            hd[i] = 1/6
        else:
            hd[i] = (1 / (np.pi * n[i])) * np.sin(np.pi * n[i] / 6)
    return hd

def window_function(N, window_type):
    n = np.arange(N)
    if window_type == 'rectangular':
        return np.ones(N)
    elif window_type == 'hamming':
        return 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    elif window_type == 'hann':
        return 0.5 - 0.5 * np.cos(2 * np.pi * n / (N - 1))
    else:
        raise ValueError("Unsupported window type")

def design_filter(N, window_type):
    M = (N - 1) // 2
    n = np.arange(-M, M + 1)
    hd = ideal_impulse_response(n)
    w = window_function(N, window_type)
    h = hd * w
    return h

def plot_response(h, N, window_type):
    w, H = np.linspace(-np.pi, np.pi, 1024, retstep=True)
    H = np.fft.fftshift(np.fft.fft(h, 1024))
    H_mag = np.abs(H)
    H_phase = np.angle(H)
    
    plt.figure(figsize=(12, 5))

    
    plt.subplot(1, 2, 1)
    plt.plot(w, H_mag)
    plt.title(f'Magnitude Response (N={N}, {window_type.title()} Window)')
    plt.xlabel('Frequency (rad/sample)')
    plt.ylabel('Magnitude')
    plt.grid(True)


    plt.subplot(1, 2, 2)
    plt.plot(w, H_phase)
    plt.title(f'Phase Response (N={N}, {window_type.title()} Window)')
    plt.xlabel('Frequency (rad/sample)')
    plt.ylabel('Phase (radians)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()


N_values = [7, 25, 125]
window_types = ['rectangular', 'hamming', 'hann']

for N in N_values:
    for window_type in window_types:
        h = design_filter(N, window_type)
        print(f'Filter Coefficients (N={N}, {window_type.title()} Window):\n{h}\n')
        plot_response(h, N, window_type)