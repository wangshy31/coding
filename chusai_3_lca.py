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
	def __init__(self, to, cost, num):
		self.to = to
		self.cost = cost
		self.num = num


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

all_path = {}
def dfs(paths, start):
	stack = [(start, [start])]
	visited = set()
	while stack:
		(node, path) = stack.pop()
		if node not in visited:
			visited.add(node)
			all_path[node] = path
			print "node:"
			print node, all_path[node]
			for ids in range(len(paths[node])):
				to = paths[node][ids].to
				if to not in visited:
					stack.append((to, path+[to]))



dfs(paths, 1)
#for i in range(m):
#	base_cost = base
#	path = dfs(paths, ques[i][0], ques[i][1])
#	if len(path) == 1:
#		print base_cost
#	else:
#		for j in range(1, len(path)):
#			nodes = paths[path[j-1]]
#			for node in nodes:
#				if node.to == path[j]:
#					if node.num % 2 == 0:
#						base_cost = base_cost + node.cost % mod_num
#					else:
#						base_cost = base_cost + mod_num - node.cost % mod_num
#		print base_cost % mod_num
#
