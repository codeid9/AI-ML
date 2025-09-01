import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([10, 20])

# Broadcast b across rows of a
result = a + b  # [[11 22], [13 24]]

print(result)