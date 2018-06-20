#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

const int P = 1000000007;

struct node {
        node *next;
        int where, cost, bound;
} *first[100001], a[200001];

int n, m, dist[100001], l, c[100001], f[100001][21], g[100001], v[100001][21], pa[100001][21];

inline void makelist(int x, int y, int z, int k) {
    a[++l].where = y;
    a[l].cost = z;
    a[l].bound = k;
    a[l].next = first[x];
    first[x] = &a[l];
}

int lca(int x, int y) {
    if (dist[x] < dist[y])
        swap(x, y);
    int jump = dist[x] - dist[y];
    for (int i = 0; jump; jump >>= 1, ++i)
        if (jump & 1)
            x = pa[x][i];
    if (x == y)
        return x;
    for (int i = 20; i >= 0; --i)
        if (pa[x][i] != pa[y][i])
            x = pa[x][i], y = pa[y][i];
    return pa[x][0];
}

int calc(int x, int y) {
    int jump = dist[x] - dist[y], will = 0;
    for (int i = 20; i >= 0; --i)
        if (jump >= (1 << i))
            jump -= 1 << i,
                 will += v[x][i], will %= P,
                 will -= f[x][i], will += P, will %= P, x = pa[x][i];
    return will;
}

int main() {
    scanf("%d", &n);
    memset(first, 0, sizeof(first));
    l = 0;
    int base = 0;
    for (int i = 1; i < n; i++) {
        int x, y, z, k;
        scanf("%d%d%d%d", &x, &y, &z, &k);
        makelist(x, y, z, k);
        makelist(y, x, z, k);
        base += 1LL * (k + (k & 1)) * z % P;
        base %= P;
    }
    memset(pa, 0, sizeof(pa));
    memset(dist, 0, sizeof(dist));
    memset(v, 0, sizeof(v));
    memset(f, 0, sizeof(f));
    c[1] = 1; dist[1] = 1;
    for (int k = 1, l = 1; l <= k; l++) {
        int m = c[l];
        for (node *x = first[m]; x; x = x->next){
            cout<<"k is : "<<k<<" ";
            cout<<"l is : "<<l<<" ";
            cout<<"where is: "<<x->where<<" ";
            cout<<"next is : "<<x->next<<" ";
            cout<<"dist is : "<<dist[x->where]<<endl;
            if (!dist[x->where])
                dist[x->where] = dist[m] + 1, c[++k] = x->where,
                    pa[x->where][0] = m;
        }
    }
    for (int i = n; i >= 1; i--) {
        int m = c[i]; f[m][0] = 0;
        for (node *x = first[m]; x; x = x->next)
            if (dist[x->where] == dist[m] + 1)
                f[x->where][0] = 1LL * ((x->bound) + (x->bound & 1)) * x->cost % P,
                    v[x->where][0] = 1LL * ((x->bound) + ((x->bound & 1) ^ 1)) * x->cost % P;
    }
    for (int i = 1; i <= 20; i++)
        for (int j = 1; j <= n; j++)
            if (pa[j][i - 1])
                pa[j][i] = pa[pa[j][i - 1]][i - 1],
                    f[j][i] = (f[j][i - 1] + f[pa[j][i - 1]][i - 1]) % P,
                                                                                                                                            v[j][i] = (v[j][i - 1] + v[pa[j][i - 1]][i - 1]) % P;
                                                            scanf("%d", &m);
                                                                for (int i = 1; i <= m; i++) {
                                                                            int x, y;
                                                                                    scanf("%d%d", &x, &y);
                                                                                            int z = lca(x, y), ans = base;
                                                                                                    ans += calc(x, z); ans %= P;
                                                                                                            ans += calc(y, z); ans %= P;
                                                                                                                    printf("%d\n", ans);
                                                                                                                        }
}
