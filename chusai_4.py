#coding=utf-8
import sys
n = 0
m = 0
k = 0
count = 0

paths = {}
nodes = []
for line in sys.stdin:
	a = line.split()
	if count == 0:
		n = int(a[0])
		m = int(a[1])
		k = int(a[2])
		for i in range(n):
			for j in range(m):
				paths[str(i)+str(j)] = []
	elif count > 0 and count <= n :
		a = str(a[0])
		for i in range(m-1):
			key_value = str(count - 1) + str(i)
			if a[i] == '0':
				paths[key_value].append([count - 1, i+1])
				paths[str(count-1)+str(i+1)].append([count-1, i])
	elif count > n and count < 2*n:
		a = str(a[0])
		for i in range(m):
			key_value = str(count - n - 1) + str(i)
			if a[i] == '0':
				paths[key_value].append([count - n, i])
				paths[str(count-n)+str(i)].append([count-n-1, i])
	else:
		nodes.append([int(a[0]) - 1, int(a[1]) - 1])
	count = count + 1


def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])
    return C[u]


def union(C, R, u, v):
    u, v = find(C, u), find(C, v)
    if R[u] > R[v]:
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:
        R[v] += 1


def kruskal(G):
    sum_weight = 0.0
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C, R = {u: u for u in G}, {u: 0 for u in G}
    for cost, u, v in sorted(E):
        if find(C, u) != find(C, v):
            T.add((u, v))
            union(C, R, u, v)
            sum_weight = sum_weight + cost
    return cost

k = kruskal(G)
print k
hello

