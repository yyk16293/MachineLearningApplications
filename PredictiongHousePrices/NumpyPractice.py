import numpy as np

my_list = [1,2,3,4]

sample_np_array = np.array(my_list)

print sample_np_array
print type(sample_np_array)

one2Darray = np.ones((4, 3)) # an 2D array with 4 "rows" and 3 "columns"
print one2Darray
print one2Darray.shape

#printing third element in rows 0 and 1
print one2Darray[0:2,2]

#dot product of arrays
array1 = np.array([2., 3., 4., 5.])
array2 = np.array([2., 3., 4., 5.])
print np.dot(array1, array2)

#product of arrays
print array1*array2

print np.sum(array1*array2)

#Euclidean length of a vector
print np.sqrt(np.dot(array1,array2))
print np.sqrt(np.sum(array1*array2))
