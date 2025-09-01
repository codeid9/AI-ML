import numpy as np

x = np.array([1,2,3,4,5])

# Element-wise
add_1 = x+1
multiply_4 = x*4

# universal functions
square=np.pow(x,2)
square_root = np.sqrt(x)

# dot product
a = np.array([1,2])
b = np.array([3,4])
dot_product = np.dot(a,b)

# Matrix multiplication
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
multiplication = np.matmul(A,B)

