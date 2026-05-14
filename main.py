#---------Digiskills Leacture number 50--------


import numpy as np #import numpy library as np
import time #import time library

# arr = np.array([[1,2,3],[3,2,1]]) #declare a array
# print(arr) #print the array

# print(arr.shape) # Print the sape of the array means number of rows and columns
# print(arr.size) #print the the size of the array
# print(arr.ndim) #Print the deminsion of the array
# print(arr.dtype) # Print the type of the array

#as we already discuss numpy reduce the time below code is manual code without numpy
# py_list = list(range(1_000_000))
# py_result =[]
# start_time = time.time()
# for i in py_list:
#     py_result.append(i+5)
# end_time =time.time()
# print("Python lis time is: ", end_time-start_time)

#Same work with numpy
# np_array =np.arange(1_000_000)
# start_time = time.time()
# np_result = np_array + 5
# end_time = time.time()
# print("Python lis time is: ", end_time-start_time)




#---------Digiskills Leacture number 51--------

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)

#print(np.zeros((3,3)))

print(np.ones((3,3)))

print(np.diag((1,1,1)))

print(np.full((3,3),7))


#---------Digiskills Leacture number 52 Numpy Array indexing slicing--------
