#coding=utf-8
import sys
import time
T = int(sys.stdin.readline().strip())
for i in range(T):
    [N, Q] = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    num = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    pre = [0 for x in range(N)]
    count_list = [0 for x in range(20000001)]
    result = {}

    q = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    print 'Case #%s: ' % str(i+1)
    pre[0] = num[0]
    for j in range(1, len(num)):
        pre[j] = pre[j-1] + num[j]
        count_list[pre[j]] = count_list[pre[j]] + 1

    for j in range(len(num)):
        for m in range(j+1, len(num)):
            count_list[pre[m] - pre[j]] =  count_list[pre[m] - pre[j]] + 1

    for j in range(20000001):
        if count_list[j] > 0:
            result[j] = count_list[j]

    sort_keys = sorted(result.keys())
    l_index = 0
    r_index = 0
    base = 0
    for j in range(len(sort_keys)):
        base = base + result[sort_keys[j]]
        if base >= q[0]:
            result[sort_keys[j]] =  base - q[0] + 1
            l_index = i
            break
    base = 0
    for j in range(len(sort_keys)):
        tmp = base
        base = base + result[sort_keys[j]]
        if tmp < q[1] and base >= q[1]:
            result[sort_keys[j]] =  q[1] - tmp
            r_index = j
            break
    result_sum = 0
    for j in range(l_index, r_index+1):
        result_sum = result_sum + result[sort_keys[j]] * sort_keys[j]
    print result_sum




