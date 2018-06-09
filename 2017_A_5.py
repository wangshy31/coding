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

def is_coprime(a,b):
	if a==0 or b==0:
		return False
    if a==1 or b==1:
        return True
	tmp = 0
	while(b!=0):
		tmp = b;
		b = a % b
		a = tmp
	if a==1:
		return True
	else:
		return False


vis = [0]*n
for i in range(m):
	begin = questions[i][0]
	end = questions[i][1]
	target = questions[i][2]
    for i in range(num_min, num_max+1):
        vis[i] = 0
	for j in range(begin-1, end):
        vis[]
			dic[num[j]] = dic[num[j]]+1
		else:
			dic[num[j]] = 1
	result = 0
	for item in dic.keys():
		if is_coprime(dic[item], target):
			result = result+1
	print result

