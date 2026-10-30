# NumPy is a Python library used for:fast calculation, working with arrays, handling number in large amounts 

# adding element of arra using numpy

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([3, 4, 5])

print(arr1 + arr2)

#printing numbers of array 

arr3 = np.array([1,2,3,4,5])
print(arr3[0:3])

#getting size of array
print(arr3.shape)

#adding one to every element of array 
print(arr3+1)

#dot product of matrices 
m1=np.array([[1,2],[3,4]])
m2=np.array([[5,6],[7,8]])
print(np.dot(m1, m2))

#finding mean of array
print(np.mean(arr3))

#getting random numbers 
print(np.random.rand(5))

