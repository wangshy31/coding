
#coding=utf-8
import sys
n = 0
m = 0
k = 0
c = 0
count = 0
weight = []
weight_sum = 0.0
scores = []
index_x = 0
index_y = 0
for line in sys.stdin:
	a = line.split()
	if count == 0:
		n = int(a[0])
		m = int(a[1])
		k = int(a[2])
		c = int(a[3])
	elif count == 1:
		for item in a:
			weight.append(int(item))
			weight_sum = weight_sum + int(item)
	else:
		tmp = []
		for item in a:
			tmp.append(int(item))
			if int(item) == -1:
				index_x = count - 2
				index_y = len(tmp) - 1
		scores.append(tmp)
	count = count + 1
for i in range(len(weight)):
	weight[i] = weight[i]*1.0 / weight_sum

max_scores = [0]*m
for i in range(m):
	for j in range(len(scores)):
		if scores[j][i] > max_scores[i]:
			max_scores[i] = scores[j][i]

result_min = []
result_max = []
if c<=max_scores[index_y]:
	for i in range(len(scores)):
		final_score = 0.0
		if i == index_x:
			final_score_min = 0.0
			final_score_max = 0.0
			for j in range(m):
				if max_scores[j] > 0:
					if j == index_y:
						final_score_max = final_score_max + weight[j]*c*1.0/max_scores[j]
					else:
						final_score_max = final_score_max + weight[j]*scores[i][j]*1.0/max_scores[j]
						final_score_min = final_score_min + weight[j]*scores[i][j]*1.0/max_scores[j]
			result_min.append(final_score_min)
			result_max.append(final_score_max)
		else:
			for j in range(m):
				if max_scores[j] > 0.0:
					final_score = final_score + weight[j]*scores[i][j]*1.0/max_scores[j]
			result_min.append(final_score)
			result_max.append(final_score)
else:
	for i in range(len(scores)):
		final_score_min = 0.0
		final_score_max = 0.0
		if i == index_x:
			for j in range(m):
				if j == index_y:
					final_score_min = final_score_min + weight[j]*1.0
					final_score_max = final_score_max + weight[j]*1.0
				else:
					if max_scores[j]>0.0:
						final_score_min = final_score_min + weight[j]*scores[i][j]*1.0/max_scores[j]
						final_score_max = final_score_max + weight[j]*scores[i][j]*1.0/max_scores[j]
		else:
			for j in range(m):
				if j == index_y:
					final_score_min = final_score_min + weight[j]*scores[i][j]*1.0/c
					final_score_max = final_score_max + weight[j]*scores[i][j]*1.0/max_scores[j]
				else:
					if max_scores[j]>0.0:
						final_score_min = final_score_min + weight[j]*scores[i][j]*1.0/max_scores[j]
						final_score_max = final_score_max + weight[j]*scores[i][j]*1.0/max_scores[j]
		result_min.append(final_score_min)
		result_max.append(final_score_max)

a = sorted(result_min, reverse=True)
flag = False
for i in range(n):
	if i != k-1 and result_min[i]==result_min[k-1]:
		flag = True
if flag:
	for i in range(len(result_min)):
		if result_min[i]>a[k-1]:
			result_min[i] = 1
		elif result_min[i]==a[k-1]:
			result_min[i] = 3
		else:
			result_min[i] = 2
else:
	for i in range(len(result_min)):
		if result_min[i]>= a[k-1]:
			result_min[i] = 1
		else:
			result_min[i] = 2


a = sorted(result_max, reverse=True)
flag = False
for i in range(n):
	if i != k-1 and result_max[i]==result_max[k-1]:
		flag = True
if flag:
	for i in range(len(result_max)):
		if result_max[i]>a[k-1]:
			result_max[i] = 1
		elif result_max[i]==a[k-1]:
			result_max[i] = 3
		else:
			result_max[i] = 2
else:
	for i in range(len(result_max)):
		if result_max[i]>= a[k-1]:
			result_max[i] = 1
		else:
			result_max[i] = 2

print_result = ''

for i in range(n):
	if result_min[i]==result_max[i]:
		print result_min[i]
	else:
		print '3'
