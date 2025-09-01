import numpy as np

arr = np.array([1,2,3,4,5,6,7])

# basic slicing
basic_slice = arr[1:4]

# boolean masking
mask = arr > 4
mask_slice = arr[mask]

# fancy indexing
index_slice=arr[[0,2,4]]

