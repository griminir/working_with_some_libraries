import numpy as np

# an array in an array is called a matrix or a 2 dimentional array
np_array = np.array([[1,2,3], [2,5,6]])
print(np_array)
print(type(np_array))
print(np_array.shape)

np_array = np.zeros((3,4), dtype=int)
np_array = np.ones((3,4), dtype=int)
np_array = np.full((3,4), 5, dtype=int)
np_array = np.random.random((3,4))
print(np_array)
# print(np_array[0,0])
# print(np_array > 0.2)
print(np_array[np_array > 0.2])
print(np.sum(np_array))

# real world example
dimensions_inch = np.array([5,6,7])
dimensions_cm = dimensions_inch * 2.54
#done with pure python
# dimensions_cm = [x * 2.54 for x in dimensions_inch] 
print(dimensions_inch, dimensions_cm)