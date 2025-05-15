import numpy as np

Z=np.zeros(10)
Z[4]=1
Z[7]=1
print(Z)

Y=np.arange(10,50)
Y=Y[::-1]
print(Y)

Y=np.arange(9).reshape(3,3)
print(Y)

nz=np.random.random((3,3,3))
print(nz)

ny=np.random.random((10,10))
print(ny.min())
print(ny.max())

nx=np.ones((4,4))
nx[1:-1,1:-1]=0
print(nx)

yn=np.diag(1+np.arange(3),k=0)
print(yn)


xn=np.random.randint(10)
xn.sort()
print(xn)