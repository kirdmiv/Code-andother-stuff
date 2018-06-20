#include "bits/stdc++.h"
#define pb push_back
#define bend(_x) begin(_x), end(_x)
#define szof(_x) ((int) (_x).size())

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int INF = 1e9 + 7;
const double PI = atan2(0, -1);
const int MAXN = 1e6, bd = 20;

int binarniyverh[bd][MAXN];
vector<int> graph[MAXN];
int depth[MAXN];

int dfs(int v, int p, int d) {
    depth[v] = d;
    binarniyverh[0][v] = p;
    for (int i = 1; i < bd; ++i) {
        binarniyverh[i][v] = binarniyverh[i - 1][binarniyverh[i - 1][v]];
    }

    for (int to: graph[v]) {
        if (to != p) {
            dfs(to, v, d + 1);
        }
    }
    return 0;
}

int get_lca(int a, int b) {
    if (depth[a] < depth[b]) {
        swap(a, b);
    }
    for (int i = bd - 1; i >= 0; --i) {
        if (depth[a] - (1 << i) >= depth[b]) {
            a = binarniyverh[i][a];
        }
    }
    if (a == b) {
        return a;
    }
    for (int i = bd - 1; i >= 0; --i) {
        if (binarniyverh[i][a] != binarniyverh[i][b]) {
            a = binarniyverh[i][a];
            b = binarniyverh[i][b];
        }
    }
    return binarniyverh[0][a];
}

int verh(int v, int l) {
    for (int i = bd - 1; i >= 0; --i) {
        if (l >= (1 << i)) {
            l -= (1 << i);
            v = binarniyverh[i][v];
        }
    }
    return v;
}

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n - 1; ++i) {
        int a, b;
        scanf("%d%d", &a, &b);
        --a; --b;
        graph[a].pb(b);
        graph[b].pb(a);
    }

    dfs(0, 0, 0);

    int q;
    scanf("%d", &q);

    for (int i = 0; i < q; ++i) {
        int a, b;
        scanf("%d%d", &a, &b);
        --a; --b;
        int lca = get_lca(a, b);
        if (depth[lca] < depth[a]) {
            cout << binarniyverh[0][a] + 1 << "\n";
        } else {
            cout << verh(b, depth[b] - depth[a] - 1) + 1 << "\n";
        }
    }
    return 0;
}
