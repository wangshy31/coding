import sys
import bisect
T = sys.stdin.readline().strip('\n')
T = int(T)
for ca in range(T):
    tmp = sys.stdin.readline().strip('\n').split(' ')
    [N, O, D] = [int(x) for x in tmp]
    tmp = sys.stdin.readline().strip('\n').split(' ')
    [x1, x2, a, b, c, m, l] = [int(x) for x in tmp]
    x = [x1, x2]
    s = [x1+l, x2+l]
    ss = [s[0], sum(s[:])]
    so = [s[0]%2, s[0]%2+s[1]%2]
    max_index = -1
    max_num = -1
    for i in range(N):
        x.append((a*x[-1] + b*x[-2] + c) % m)
        s.append(x[-1]+l)
        ss.append(ss[-1]+s[-1])
        so.append(so[-1]+s[-1]%2)
        if s[-1] <= D and s[-1]%2 <= O and s[-1]>max_num:
            max_index = i
            max_num = s[-1]
    if max_index < 1:
        print 'Case #%s: '%ca,
        print 'IMPOSSIBLE'

    for i in range(N):
        if ss[i] > D or so[i] > O:
            break
        else:
            max_index = i
            max_num = ss[i]



    print 'Case #%s: '%ca,
    if max_num < 0:
        print 'IMPOSSIBLE'
    else:
        print max_num




