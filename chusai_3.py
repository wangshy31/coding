#coding=utf-8
import sys
n = 0
m = 0
path = []
ques = []
count = 0
for line in sys.stdin:
	a = line.split()
	if count == 0:
		n = int(a[0])
	elif count > 0 and count < n:
		tmp = []
		for item in a:
			tmp.append(int(item))
		path.append(tmp)
	elif count == n:
		m = int(a[0])
	else:
		tmp = []
		for item in a:
			tmp.append(int(item))
		ques.append(tmp)
	count = count + 1
print n, path, m, ques

all_path = {}
for i in range(path):
	if path[i][0] in all_path.keys():
		all_path[path[i][0]].append([path[i][1], path[i][2], path[i][3]])
    else:
    	all_path[path[i][0]] = []
		all_path[path[i][0]].append([path[i][1], path[i][2], path[i][3]])

	if path[i][1] in all_path.keys():
		all_path[path[i][1]].append([path[i][0], path[i][2], path[i][3]])
    else:
    	all_path[path[i][1]] = []
		all_path[path[i][1]].append([path[i][0], path[i][2], path[i][3]])




for i in range(ques):

