#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <utility>
#include <functional>
#include <set>
#include <string>
#include <math.h>
#include <cmath>
#include <queue>

#define mp make_pair
#define ff first
#define ss second
#define ll long long
#define pb push_back
#define st size_t

using namespace std;

vector < vector<int> > g;
int n;

vector<int> bfs(int s){
    queue<int> q;
    q.push(s);
    vector<bool> used(n);
    vector<int> d(n);
    d[s] = 0;
    used[s] = true;
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (size_t i=0; i<g[v].size(); i++) {
            int to = g[v][i];
            if (!used[to]) {
                used[to] = true;
                q.push(to);
                d[to] = d[v] + 1;
            }
        }
    }
    return d;
}

int main()
{
    int k;
    const int INF = 1e9;
    cin >> n >> k;
    int a, b;
    g.resize(n);
    for (int i = 0; i< n-1; i++){
        cin >> a >> b;
        a--;b--;
        g[a].pb(b);
        g[b].pb(a);
    }
    vector< vector<int> > dist(n);
    for (st i = 0; i < n; i++)
        dist[i] = bfs(i);
    vector<bool> used(n, false);
    int v, u, w;
    v = u = w = 0;
    for (int i = 0; i < n; i++)
         if (dist[0][i] > dist[0][u])
              u = i;
    for (int i = 0; i < n; i++)
          if (dist[u][i] > dist[u][w])
               w = i;
    used[u] = true;
    used[w] = true;
    cout << u+1 << " " << w+1 << " ";
    int cur_ans = dist[u][w], res1 = 0, res2 = 0, ind = 0;
    for (int x = 2; x < k; x++){
        res2 = -1;
        ind = 0;
        for (int i = 0; i < n; i++){
            res1 = INF;
            if (!used[i]){
                for (int j = 0; j < n; j++){
                    if(used[j])
                        res1 = min(res1, dist[j][i]);
                }
                if (res2 < res1){
                    res2 = res1;
                    ind = i;
                }
            }
        }
        cur_ans = min(cur_ans, res2);
        used[ind] = true;
        cout << ind + 1 << " ";
    }
    cout << cur_ans;
}

