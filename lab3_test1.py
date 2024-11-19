import numpy as np

x = np.array([1, 2, 3, 4])
n1 = np.arange(-1, 3)  

h = np.array([1, 2, 1, 1])
n2 = np.arange(-2, 2)  


x_reversed = x[::-1]
n1_reversed = -n1[::-1]

h_reversed = h[::-1]
n2_reversed = -n2[::-1]

# Display results
print(f"Original x(n): {x} with n = {n1}")
print(f"Time-reversed x(-n): {x_reversed} with n = {n1_reversed}")

print(f"Original h(n): {h} with n = {n2}")
print(f"Time-reversed h(-n): {h_reversed} with n = {n2_reversed}")
