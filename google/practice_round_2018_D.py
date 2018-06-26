#coding=utf-8
import sys
import time
T = int(sys.stdin.readline().strip())
for i in range(T):
    [N, Q] = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    num = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    result = []
    print 'Case #%s: ' % str(i+1)
    for m in range(len(num)):
        tmp_sum = 0
        for n in range(m, len(num)):
            tmp_sum = tmp_sum + num[n]
            result.append(tmp_sum)
    result.sort()
    for j in range(Q):
        q = [int(x) for x in sys.stdin.readline().strip().split(' ')]
        print sum(result[q[0]-1 : q[1]])


