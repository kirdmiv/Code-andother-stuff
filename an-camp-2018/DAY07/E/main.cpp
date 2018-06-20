#include <vector>
#include <set>
#include <iostream>


using namespace std;

struct Edge {
    long long a, b, cos;
};

using ll = long long;

const ll INF = 1e15 + 3;
set<long long> changes;
vector<bool> used;
vector<vector<long long>> g;

void dfs(long long v) {
    if (used[v]) return;
    changes.insert(v);
    used[v] = 1;
    for (long long u : g[v]) dfs(u);
}

int main() {
    freopen("path.in", "r", stdin);
    freopen("path.out", "w", stdout);
    ll n, m, s;
    cin >> n >> m >> s;
    vector<Edge> edges;
    used.resize(n + 1);
    g.resize(n + 1);
    for (long long i = 0; i < m; i++) {
        ll v1, v2, w;
        cin >> v1 >> v2 >> w;
        edges.push_back({v1, v2, w});
        g[v1].push_back(v2);
    }
    ll dist[n + 1];
    for (long long i = 0; i <= n; i++) dist[i] = INF;
    dist[s] = 0;
    for (long long i = 0; i <= n; i++) {
        for (Edge u : edges) {
            if (dist[u.a] != INF)
                dist[u.b] = min(min(dist[u.b], dist[u.a] + u.cos), INF);
        }
    }
    for (long long i = 0; i <= n; i++) {
        for (Edge u : edges) {
            if (dist[u.b] > dist[u.a] + u.cos && dist[u.a] != INF) {
                changes.insert(u.b);
                dfs(u.b);
                dist[u.b] = min(min(dist[u.b], dist[u.a] + u.cos), INF);
            }
        }
    }
    for (long long i = 1; i <= n; i++) {
        if (dist[i] >= INF)
            cout << "*" << endl;
        else if
                (changes.count(i)) cout << "-" << endl;
        else
            cout << dist[i] << endl;
    }
}
