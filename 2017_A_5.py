#coding=utf-8
import sys
n = 0
m = 0
num = []
questions = []
count = 0
num_min = 0
num_max = 0
for line in sys.stdin:
	a = line.split()
	if count == 0:
		n = int(a[0])
		m = int(a[1])
	elif count == 1:
		for item in a:
			num.append(int(item))
		num_min = min(num)
		num_max = max(num)
	else:
		questions.append([int(a[0]), int(a[1]), int(a[2])])
	count = count + 1

def computeGCD(x, y):
	while(y):
		x, y = y, x % y
	return x

for i in range(m):
	vis = [0]*(num_max - num_min+1)
	begin = questions[i][0]
	end = questions[i][1]
	target = questions[i][2]
	for j in range(begin-1, end):
		vis[num[j] - num_min] = vis[num[j] - num_min] + 1
	result = 0
	for item in vis:
		if item>0:
			if computeGCD(item, target) == 1:
				result = result+1
	print result

