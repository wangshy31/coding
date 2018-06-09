#coding=utf-8
import sys
n = 0
v = 0
u = 0
c = []
d = []
count = 0
for line in sys.stdin:
	a = line.split()
	if count == 0:
		n = int(a[0])
		v = float(a[1])
		u = float(a[2])
	elif count == 1:
		for item in a:
			c.append(float(item))
	else:
		for item in a:
			d.append(float(item))
	count = count + 1

all_sum = 0.0
for i in range(n):
	one_sum = 0.0
	for j in range(n):
		one_sum = one_sum + (u*n*1.0/(c[i] - j*d[i]-v))
	all_sum = all_sum + one_sum*1.0/n

print "%.3f"%all_sum
