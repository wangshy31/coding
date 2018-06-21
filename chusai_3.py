#coding=utf-8
import sys
n = 0
m = 0
path = []
ques = []
count = 0
base = 0
mod_num = 1000000007

class Node:
	def __init__(self, index, to, cost):
		self.index = index
		self.to = to
		self.cost = cost

paths = {}
for line in sys.stdin:
	a = line.split()
	if count == 0:
		n = int(a[0])
	elif count > 0 and count < n:
		if int(a[0]) not in paths.keys():
			paths[int(a[0])] = []
		if int(a[1]) not in paths.keys():
			paths[int(a[1])] = []
		paths[int(a[0])].append(Node(int(a[1]), int(a[2]), int(a[3])))
		paths[int(a[1])].append(Node(int(a[0]), int(a[2]), int(a[3])))
		base = base + (int(a[2])*(int(a[3]) + (int(a[3]) & 1))) % mod_num
	elif count == n:
		m = int(a[0])
	else:
		tmp = []
		for item in a:
			tmp.append(int(item))
		ques.append(tmp)
	count = count + 1
print base
print paths

