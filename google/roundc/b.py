#coding=utf-8
import sys
import time


ans = 0
def dfs(arr, visited, x, y, n, max_num, sum_num, ans):
    if x==n:
        if (max_num * 2 < sum_num):
            ans += 1



T = int(sys.stdin.readline().strip())
for i in range(T):
    n = int(sys.stdin.readline().strip())
    arr = []
    for j in range(n):
        tmp = sys.stdin.readline().strip().split(' ')
        tmp = [int(x) for x in tmp]
        arr.append(tmp)






    #print 'Case #%s:' % str(i+1),
    #print(" ".join(map(str, res[1:])))


