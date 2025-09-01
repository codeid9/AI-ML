import numpy as np


A = np.array([[1, 2], [3, 4]])

# Inverse
inv_A = np.linalg.inv(A)
# Determinant
det_A = np.linalg.det(A)

# Eigenvalues & eigenvectors
eigvals, eigvecs = np.linalg.eig(A)

# Solve Ax = b
b = np.array([5, 6])
x = np.linalg.solve(A, b)
