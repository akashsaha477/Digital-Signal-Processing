import numpy as np

arr1=np.array([[2,3],[0,9],[-2,-4]])

arr2=np.array([[-4,6],[23,-7],[1,2]])

print(arr1, "\n")

print(arr2, "\n")

print(arr1+arr2, "\n")

print(arr1-arr2, "\n")

print(arr1*arr2, "\n")

print(arr2.T, "\n")

arr3=np.transpose(arr2)

print(arr3, "\n")

print(arr1@arr3, "\n")
