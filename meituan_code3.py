#coding=utf-8
import sys
p = []
count = 0
for line in sys.stdin:
	a = line.split()
	tmp = []
	for item in a:
		tmp.append(float(item))
	p.append(tmp)

p_index = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
		   [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [3, 0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
		   [2, 0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [5, 6, 7, 0, 1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15],
		   [4, 6, 7, 0, 1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15], [7, 4, 5, 0, 1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15],
		   [6, 4, 5, 0, 1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15], [9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7],
		   [8, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7], [11, 8, 9, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7],
		   [10, 8, 9, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7], [13, 14, 15, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7],
		   [12, 14, 15, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7], [15, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7],
		   [14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7]]

result = []
tmp = []
for i in range(16):
	tmp.append(p[i][p_index[i][0]])
result.append(tmp)

tmp = []
for i in range(16):
	accu = 0.0
	for j in range(1, 3):
		tmp_index = p_index[i][j]
		accu = accu + result[0][i]*result[0][tmp_index]*p[i][tmp_index]
	tmp.append(accu)
result.append(tmp)

tmp = []
for i in range(16):
	accu = 0.0
	for j in range(3, 7):
		tmp_index = p_index[i][j]
		accu = accu + result[1][i]*result[1][tmp_index]*p[i][tmp_index]
	tmp.append(accu)
result.append(tmp)

tmp = []
for i in range(16):
	accu = 0.0
	for j in range(7, 15):
		tmp_index = p_index[i][j]
		accu = accu + result[2][i]*result[2][tmp_index]*p[i][tmp_index]
	tmp.append(accu)
result.append(tmp)

result_str = ''
for i in range(16):
	result_str = result_str + str(result[3][i])+' '
result_str = result_str[0:-1]
print result_str
