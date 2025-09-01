import numpy as np

np.random.seed(42)  # Reproducibility

# Uniform and normal
print(np.random.rand(3))     # [0.37454012 0.95071431 0.73199394]
print(np.random.randn(3))    # Normal distribution

# Random integers
print(np.random.randint(0, 10, size=5))  # [7 4 6 9 2]

# Shuffle and choice
arr = np.array([1, 2, 3, 4])
np.random.shuffle(arr)
print(arr)

print(np.random.choice(arr, size=2, replace=False))  # Random sample
