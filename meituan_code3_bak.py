#coding=utf-8
import sys
import numpy as np
p = np.zeros(shape=(16, 16), dtype=np.float32)
count = 0
for line in sys.stdin:
	a = line.split()
	b = np.array(a, dtype=np.float32)
	p[count, :] = b[0:16]
	count = count + 1

p_index = np.zeros(shape=(16, 15))
p_index[0,:] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
p_index[1,:] = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
p_index[2,:] = [3, 0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
p_index[3,:] = [2, 0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
p_index[4,:] = [5, 6, 7, 0, 1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15]
p_index[5,:] = [4, 6, 7, 0, 1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15]
p_index[6,:] = [7, 4, 5, 0, 1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15]
p_index[7,:] = [6, 4, 5, 0, 1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15]
p_index[8,:] = [9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7]
p_index[9,:] = [8, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7]
p_index[10,:] = [11, 8, 9, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7]
p_index[11,:] = [10, 8, 9, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7]
p_index[12,:] = [13, 14, 15, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7]
p_index[13,:] = [12, 14, 15, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7]
p_index[14,:] = [15, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7]
p_index[15,:] = [14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7]

result = np.zeros(shape=(4, 16), dtype = np.float32)
for i in range(16):
	result[0, i] = p[i, p_index[i, 0]]


for i in range(16):
	for j in range(1, 3):
		tmp_index = p_index[i, j]
		result[1, i] = result[1, i] + result[0, i]*result[0, tmp_index]*p[i, tmp_index]

for i in range(16):
	for j in range(3, 7):
		tmp_index = p_index[i, j]
		result[2, i] = result[2, i] + result[1, i]*result[1, tmp_index]*p[i, tmp_index]

for i in range(16):
	for j in range(7, 15):
		tmp_index = p_index[i, j]
		result[3, i] = result[3, i] + result[2, i]*result[2, tmp_index]*p[i, tmp_index]

result_str = ''
for i in range(16):
	result_str = result_str + str(result[3, i])+' '
result_str = result_str[0:-1]
print result_str
