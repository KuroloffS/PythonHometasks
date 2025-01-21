import numpy as np

# 1. Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)

# 2. Create a 3x3 matrix with values ranging from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)

# 3. Create a 3x3 identity matrix
identity_matrix = np.eye(3)

# 4. Create a 3x3x3 array with random values
array_3x3x3 = np.random.random((3, 3, 3))

# 5. Create a 10x10 array with random values and find the minimum and maximum values
array_10x10 = np.random.random((10, 10))
min_value = array_10x10.min()
max_value = array_10x10.max()

# 6. Create a random vector of size 30 and find the mean value
random_vector = np.random.random(30)
mean_value = random_vector.mean()

# 7. Normalize a 5x5 random matrix
random_matrix_5x5 = np.random.random((5, 5))
normalized_matrix = (random_matrix_5x5 - random_matrix_5x5.min()) / (random_matrix_5x5.max() - random_matrix_5x5.min())

# 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))
matrix_product_5x3_3x2 = np.dot(matrix_5x3, matrix_3x2)

# 9. Create two 3x3 matrices and compute their dot product
matrix_A = np.random.random((3, 3))
matrix_B = np.random.random((3, 3))
dot_product = np.dot(matrix_A, matrix_B)

# 10. Given a 4x4 matrix, find its transpose
matrix_4x4 = np.random.random((4, 4))
transpose_4x4 = matrix_4x4.T

# 11. Create a 3x3 matrix and calculate its determinant
matrix_3x3_for_determinant = np.random.random((3, 3))
determinant = np.linalg.det(matrix_3x3_for_determinant)

# 12. Create two matrices (A) (3x4) and (B) (4x3), and compute the matrix product (A ⋅ B)
matrix_A_3x4 = np.random.random((3, 4))
matrix_B_4x3 = np.random.random((4, 3))
matrix_product_A_B = np.dot(matrix_A_3x4, matrix_B_4x3)

# 13. Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product
matrix_3x3_random = np.random.random((3, 3))
column_vector_3x1 = np.random.random((3, 1))
matrix_vector_product = np.dot(matrix_3x3_random, column_vector_3x1)

# 14. Solve the linear system (Ax = b) where (A) is a 3x3 matrix, and (b) is a 3x1 column vector
matrix_A_for_system = np.random.random((3, 3))
b_vector = np.random.random((3, 1))
solution_x = np.linalg.solve(matrix_A_for_system, b_vector)

# 15. Given a 5x5 matrix, find the row-wise and column-wise sums
matrix_5x5 = np.random.random((5, 5))
row_wise_sums = matrix_5x5.sum(axis=1)
column_wise_sums = matrix_5x5.sum(axis=0)

# Outputs
print("Vector:", vector)
print("3x3 Matrix:\n", matrix_3x3)
print("Identity Matrix:\n", identity_matrix)
print("3x3x3 Array:\n", array_3x3x3)
print("Min Value:", min_value, "Max Value:", max_value)
print("Mean Value:", mean_value)
print("Normalized Matrix:\n", normalized_matrix)
print("Matrix Product (5x3 * 3x2):\n", matrix_product_5x3_3x2)
print("Dot Product of two 3x3 matrices:\n", dot_product)
print("Transpose of 4x4 Matrix:\n", transpose_4x4)
print("Determinant of 3x3 Matrix:", determinant)
print("Matrix Product (3x4 * 4x3):\n", matrix_product_A_B)
print("Matrix-Vector Product:\n", matrix_vector_product)
print("Solution to Linear System (Ax = b):\n", solution_x)
print("Row-wise Sums:", row_wise_sums)
print("Column-wise Sums:", column_wise_sums)
