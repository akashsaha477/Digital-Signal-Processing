import numpy as np

def convolution_manual(x, n1, h, n2):
    # Length of sequences
    len_x = len(x)
    len_h = len(h)
    
    # Folding h(n) to get h(-k)
    h_folded = np.flip(h)
    
    # Time indices after folding h(n)
    n_h_folded = -np.flip(n2)
    
    # Output sequence index range
    n_y_min = min(n1) + min(n_h_folded)
    n_y_max = max(n1) + max(n_h_folded)
    n_y = np.arange(n_y_min, n_y_max + 1)
    
    # Initialize y(n) with zeros
    y = np.zeros(len(n_y), dtype=int)
    
    # Perform convolution
    for i in range(len(n_y)):
        n_shifted_h = n_h_folded + n_y[i]
        # Overlap x(n) and h_shifted(n-k) and sum the products
        for j in range(len_x):
            if n1[j] in n_shifted_h:
                y[i] += x[j] * h_folded[np.where(n_shifted_h == n1[j])[0][0]]
                
    return y, n_y

# Given sequences and their index ranges
x = np.array([1, 5, 3, 1, 1])
n1 = np.arange(-2, 3)
h = np.array([1, 2, 1, 2])
n2 = np.arange(-1, 3)

# x=[]
# h=[]
# x_start=int(input("starting index of x(n)"))


# Perform the convolution manually
y_manual, n_y_manual = convolution_manual(x, n1, h, n2)

# Display the result
print("Manual Convolution y(n):", y_manual)
print("n:", n_y_manual)
print("Using Inbuilt Function:",np.convolve(x,h))