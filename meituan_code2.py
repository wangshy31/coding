#coding=utf-8
import sys
n = 0
m = 0
k = 0
count = 0
mei = []
tuan = []
for line in sys.stdin:
	a = line.split()
	if count == 0:
		n = int(a[0])
		m = int(a[1])
		k = int(a[2])
	else:
		mei.append(int(a[0]))
		tuan.append(int(a[1]))
	count = count + 1

result_index = 0
tmp_sum = -30000
for i in range(len(mei)):
	tmp = (m*1.0/n) * mei[i] + ((n-m)*1.0/n) * tuan[i]
	if tmp >= tmp_sum:
		tmp_sum = tmp
		result_index = i

result = ''
for i in range(k):
	if i != result_index:
		result = result + '0 '
	else:
		result = result + str(n) + ' '
result = result[0:-1]
print result



