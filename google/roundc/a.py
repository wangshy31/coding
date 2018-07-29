#coding=utf-8
import sys
import time


def dfs(paths):
    start = paths.keys()[0]
    stack = [(start, [start])]
    while stack:
        [node, path] = stack.pop()
        for next_id in range(len(paths[node])):
            next_node = paths[node][next_id]
            if next_node in set(path) and next_node != path[-2]:
                begin_id = -1
                for i in range(len(path)):
                    if path[i] == next_node:
                        return path[i:]
            if next_node not in set(path):
                stack.append((next_node, path + [next_node]))

def bfs(paths, circle, cur, visited, depth, res):
    next_node = []
    for item in cur:
        node = paths[item]
        for n in node:
                if n not in visited:
                    res[n] = depth
                    visited.add(n)
                    next_node.append(n)
    if len(next_node) == 0:
        return
    else:
        bfs(paths, circle, next_node, visited, depth+1, res)



T = int(sys.stdin.readline().strip())
for i in range(T):
    n = int(sys.stdin.readline().strip())
    dic = {}
    for j in range(n):
        [p, q] = [int(x) for x in sys.stdin.readline().strip().split(' ')]
        if p in dic:
            dic[p].append(q)
        else:
            dic[p] = [q]
        if q in dic:
            dic[q].append(p)
        else:
            dic[q] = [p]

    circle = dfs(dic)
    res = [0 for m in range(n+1)]
    visited = set(circle)
    bfs(dic, circle, circle, visited, 1, res)
    print 'Case #%s:' % str(i+1),
    print(" ".join(map(str, res[1:])))


