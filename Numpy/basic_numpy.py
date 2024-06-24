import numpy as np

# a = np.array([1, 2, 3], dtype='int32')
# print(a)
# print(a.shape)
# print(a.dtype)
# print(a.itemsize)
# print(a.nbytes) # total bytes consumed by the array (itemsize * size)

# b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
# print(b)
# print(b.shape) # shape of the matrix
# print(b.dtype) # data type of the elements
# print(b.itemsize) # size of each element in bytes

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
# print(a)
# # Get a specific element [r, c]
# print("specific element")
# print(a[0, 5])
# # Get a specific row
# print("specific row")
# print(a[0, :])
# # Get a specific column
# print("specific column")
# print(a[:, 2])

# # Getting a little more fancy [startindex:endindex:stepsize]

# print(a[0, 1:6:2])
# print(a[0, 1:-1:2])

# a[1, 5] = 20
# a[:, 2] = [1, 2]
# # print(a)

# b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(b)

# Get specific element (work outside in)

# print(b[0, 1, 1])
# print(b[:, 1, :])
# b[:, 1, :] = [[9, 9], [8, 8]]
# print(b)

# All 0s matrix
# print(np.zeros((2, 3)))

# # All 1s matrix
# print(np.ones((4, 2, 2), dtype='int32'))

# # Any other number (full)
# print(np.full((2, 2), 99, dtype='float32'))

# # Any other number (full_like)
# print(np.full_like(a, 4))

# # Random decimal numbers
# print(np.random.rand(4, 2, 3))

# print(np.random.random_sample(a.shape))

# # Random integer values

# print(np.random.randint(-4, 8, size=(3, 3))) 

# # The identity matrix
# np.identity(5)

# Repeat an array
# arr = np.array([1, 2, 3])
# r1 = np.repeat(arr, 3, axis=0)
# print(r1)

# output = np.ones((5, 5))
# print(output)

# z = np.zeros((3,3))
# z[1,1] = 9
# print(z)

# output[1:-1, 1:-1] = z
# print(output)

# Be careful when copying arrays!!!
# a = np.array([1, 2, 3])
# b = a.copy()
# b[0] = 100
# print(a)

# Mathematics

# a = np.array([1, 2, 3, 4])
# print(a)
# print(a + 2)
# print(a - 2)
# print(a * 2)
# print(a / 2)
# print(a ** 2)

# b = np.array([1, 0, 1, 0])
# print(a + b)

# Take sin cos tan cosin
# print(np.sin(a))

# Linear Algebra

# a = np.ones((2, 3))
# print(a)

# b = np.full((3,2), 2)
# print(b)

# print(np.matmul(a, b))

# # Find the determinant
# c = np.identity(3)
# print(c)
# print(np.linalg.det(c))

# Statistics

# stats = np.array([[1, 2, 3], [4, 5, 6]])
# print(stats)

# print(np.min(stats))
# print(np.max(stats, axis=1))
# print(np.sum(stats, axis=0))

# Reorganizing arrays

# before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(before)

# after = before.reshape((4, 2))
# print(after)

# # Vertically stacking vectors

# v1 = np.array([1, 2, 3, 4])
# v2 = np.array([5, 6, 7, 8])

# print(np.vstack([v1, v2, v1, v2]))

# # Horizontal stack
# h1 = np.ones((2, 4))
# h2 = np.zeros((2, 2))

# print(np.hstack((h1, h2)))

# Load data from file

fileData = np.genfromtxt('data.txt', delimiter=',')
fileData = fileData.astype('int32')
print(fileData)

# Boolean masking and advanced indexing

# print(fileData > 50)
# print(fileData[fileData > 50])

# Index with a list in numpy

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(a[[1, 2, 8]])

print(np.any(fileData > 50, axis=0)) #any

# print(~((fileData > 50) & (fileData < 100)))
      