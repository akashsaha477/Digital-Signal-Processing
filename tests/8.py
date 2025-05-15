import numpy as np

# Define the matrix A
A = np.array([[1+1j, 2-1j, 3], 
              [0, 9+2j, 8], 
              [-2+1j, -4, 1-1j]])


det_A = np.linalg.det(A)
print(det_A,"\n")


conj_A = np.conjugate(A)
print(conj_A,"\n")

transpose_A = np.transpose(A)
print(transpose_A,"\n")


hermitian_A = np.conjugate(np.transpose(A))
print(hermitian_A,"\n")


inverse_A = np.linalg.inv(A)
print(inverse_A,"\n")


