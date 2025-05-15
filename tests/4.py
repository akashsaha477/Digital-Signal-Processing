import numpy as np
A=np.array([1,2,3,4,5,6,7,8,9,10])
print(A)
print(A[::2])
upsampled = np.repeat(A, 2)
print(upsampled)
print(np.sum(A))
print(np.average(A))