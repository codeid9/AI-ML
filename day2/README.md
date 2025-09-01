# 🧠 Practical NumPy Topics for AI/ML

This guide covers only the essential NumPy concepts you'll use in real-world AI and ML projects—from data preprocessing to model optimization. Each section is designed for hands-on practice and modular reuse.

---

## ✅ Table of Contents

- Array Creation
- Array Indexing & Slicing
- Reshaping & Manipulation
- Broadcasting
- Mathematical Operations
- Aggregation Functions
- Random Number Generation
- Linear Algebra Essentials
- Performance Optimization

---

## 1. 🔢 Array Creation

- `np.array()`: Create arrays from lists
- `np.zeros()`, `np.ones()`: Initialize arrays with fixed values
- `np.arange()`, `np.linspace()`: Generate sequences
- Specify data types with `dtype`

---

## 2. 🔍 Array Indexing & Slicing

- Access elements: `arr[0]`, `arr[1:5]`
- Boolean masking: `arr[arr > 0]`
- Fancy indexing: `arr[[0, 2, 4]]`

---

## 3. 🔄 Reshaping & Manipulation

- `reshape()`, `ravel()`, `flatten()`: Change array shape
- `transpose()`: Flip axes
- Stacking: `np.vstack()`, `np.hstack()`

---

## 4. 📐 Broadcasting

- Apply operations across arrays of different shapes
- Add scalar to array: `arr + 5`
- Element-wise operations with shape alignment

---

## 5. ➕ Mathematical Operations

- Element-wise: `+`, `-`, `*`, `/`
- Universal functions: `np.exp()`, `np.log()`, `np.sqrt()`
- Dot product: `np.dot()`, `@`
- Matrix multiplication: `np.matmul()`

---

## 6. 📊 Aggregation Functions

- `np.sum()`, `np.mean()`, `np.std()`, `np.min()`, `np.max()`
- Axis-based operations: `axis=0`, `axis=1`

---

## 7. 🎲 Random Number Generation

- `np.random.rand()`, `np.random.randn()`: Uniform and normal distributions
- `np.random.randint()`: Random integers
- `np.random.seed()`: Reproducibility

---

## 8. 🧮 Linear Algebra Essentials

- `np.linalg.inv()`: Matrix inversion
- `np.linalg.det()`: Determinant
- `np.linalg.eig()`: Eigenvalues and eigenvectors
- `np.linalg.solve()`: Solve linear systems

---

## 9. 🚀 Performance Optimization

- Use vectorized operations instead of loops
- Avoid unnecessary copies
- Profile with `%timeit` in Jupyter

---

## 🧠 Final Note

These topics form the backbone of efficient AI/ML workflows. Practice each with real datasets, modularize your scripts, and share your insights with the community!
