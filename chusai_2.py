#coding=utf-8
import sys
n = 0
source = []
target = []
c = []
count = 0
for line in sys.stdin:
	a = line.split()
	if count == 0:
		n = int(a[0])
	elif count == 1:
		for item in a:
			source.append(int(item))
	else:
		for item in a:
			target.append(int(item))
	count = count + 1

for i in range(len(source)):
	c.append(source[i] - target[i])

result = 0
for i in reversed(range(1, len(source))):
	if c[i] > 0:
		result = result + c[i]
		c[i-1] = c[i-1] + c[i]
		c[i] = 0

if c[0]>0:
	for i in range(0, len(source)-1):
		if c[i] > 0:
			result = result + c[i]
			c[i+1] = c[i+1]+c[i]
			c[i] = 0
print result
