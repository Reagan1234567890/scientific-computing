import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)

print("Array + 2:", arr + 2)
print("Array * 3:", arr * 3)
print("Array squared:", arr ** 2)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(matrix)

print("\nTransposed Matrix:")
print(matrix.T)

reshaped = np.arange(1, 10).reshape(3, 3)
print("\nReshaped 3x3 Matrix:")
print(reshaped)

matrix2 = np.array([[7, 8], [9, 10], [11, 12]])
result = np.dot(matrix, matrix2)
print("\nMatrix Multiplication Result:")
print(result)

print("\nMean of matrix:", np.mean(matrix))
print("Standard deviation of matrix:", np.std(matrix))
