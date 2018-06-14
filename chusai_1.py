#coding=utf-8
import sys
T = 0
film = []
count = 0
for line in sys.stdin:
	a = line.split()
	if count == 0:
		T = int(a[0])
	else:
		film.append(a)
	count = count + 1


step1 = [1,2,1,2,3,2,3,4]
step2 = [[0,1,2,1,2,3,2,3],
		 [1,0,3,2,1,4,3,2],
		 [2,3,0,1,2,1,2,3],
		 [1,2,1,0,1,2,1,2],
		 [2,1,2,1,0,3,2,1],
		 [3,4,1,2,3,0,1,2],
		 [2,3,2,1,2,1,0,1],
		 [3,2,3,2,1,2,1,0]]
def find_index(s):
	if s=='A' or s=='B' or s=='C':
		return 0
	elif s=='D' or s=='E' or s=='F':
		return 1
	elif s=='G' or s=='H' or s=='I':
		return 2
	elif s=='J' or s=='K' or s=='L':
		return 3
	elif s=='M' or s=='N' or s=='O':
		return 4
	elif s=='P' or s=='Q' or s=='R' or s=='S':
		return 5
	elif s=='T' or s=='U' or s=='V':
		return 6
	else:
		return 7
for i in range(len(film)):
	count = 0
	name = film[i][0]
	for j in range(len(name)):
		if j == 0:
			count = count + step1[find_index(name[j])]
		else:
			count = count + step2[find_index(name[j-1])][find_index(name[j])]
	print count




