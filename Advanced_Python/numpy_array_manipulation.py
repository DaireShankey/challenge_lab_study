# numpy_operations.py
import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])

# Perform element-wise operations
arr_squared = arr ** 2
print("Squared array:", arr_squared)

# Reshape array
arr_reshaped = arr.reshape((5, 1))
print("Reshaped array:\n", arr_reshaped)

# Create a 2D array and perform matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
product = np.dot(matrix1, matrix2)
print("Matrix product:\n", product)
