import numpy as np 

data = np.array([[1, 2], [3, 4]])

print(np.sum(data))         # 10
print(np.mean(data))        # 2.5
print(np.std(data))         # 1.118
print(np.min(data))         # 1
print(np.max(data))         # 4

# Axis-based
print(np.sum(data, axis=0))  # [4 6]
print(np.sum(data, axis=1))  # [3 7]

