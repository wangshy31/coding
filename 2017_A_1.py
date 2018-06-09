#coding=utf-8
import sys
n = 0
t = 0
c = 0
all_node = []
count = 0
for line in sys.stdin:
	a = line.split()
	if count == 0:
		n = int(a[0])
	elif count == 1:
		t = int(a[0])
		c = int(a[1])
	else:
		all_node.append([int(a[0]), int(a[1])])
	count = count + 1


hot = 0.0
cold = 0.0
sum_tc = 0
sum_c = 0
cup_min = 10000.0
cup_max = 0.0
for i in range(len(all_node)):
	sum_tc = sum_tc + all_node[i][0]* all_node[i][1]
	sum_c = sum_c + all_node[i][1]
	if all_node[i][0]> cup_max:
		cup_max = all_node[i][0]
	if all_node[i][0]< cup_min:
		cup_min = all_node[i][0]

all_aver = (sum_tc+t*c)*1.0/(sum_c+c)


if t >= cup_max:
	if all_aver>=cup_max:
		print 'Possible'
		print("%.4f" % all_aver)
	else:
		print 'Impossible'
elif t<=cup_min:
	if all_aver<=cup_min:
		print 'Possible'
		print("%.4f" % cup_min)
	else:
		print 'Impossible'
else:
	print 'Impossible'

