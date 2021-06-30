import time

import numpy as np

start_time = time.time()
data_array = np.arange(10000000)
print("NumPy Array %s seconds to create" %
      (time.time() - start_time))

start_time = time.time()
data_list = list(range(10000000))
print("Built-in List %s seconds to create" % (time.time() - start_time))

print('Multiple each sequence by 2')

start_time = time.time()
data_array = data_array * 2
print("NumPy Array %s seconds to process" % (time.time() - start_time))

start_time = time.time()
data_list = [x * 2 for x in data_list]
print("Built-in List %s seconds to process" % (time.time() - start_time))
