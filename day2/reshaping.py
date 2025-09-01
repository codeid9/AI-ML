import numpy as np

arr = np.arange(6)

 
reshaped = arr.reshape((2,3))

flat = reshaped.flatten()

transposed=reshaped.transpose()

# stack vertically/horizontally
a=np.array([1,2,3])
b=np.array([4,5,6])
vstacked=np.vstack((a,b))
hstacked=np.hstack((a,b))


