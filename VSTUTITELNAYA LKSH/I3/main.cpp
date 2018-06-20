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
int n;
vector < vector<int> > g;

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

vector<bool> used1;
vector<bool> used2;
const int INF = 1e9;

int dfs(int v, int cur, int dist){
    if(used1[v])
        return cur;
    used1[v]= true;
    for(int i = 0; i < g[v].size(); i++){
        cur = min(cur, dfs(g[v][i], cur+1, dist));
    }
    if(cur >= dist){
        used2[v] = true;
        return 1;
    }
    //if (v == 1)
        //cout << endl << cur << endl;
    return cur+1;
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
    vector<int> d = bfs(0);
    int mx = 0, ind = 0;
    for (int i = 0; i < n; i ++){
        if (d[i] > mx){
            ind = i;
            mx = d[i];
        }
    }
    //for (int i = 0; i < n; i++)
        //cout << d[i] << " ";
    //cout << endl << ind << endl;
    int cu = 1;
    used1.resize(n);
    used2.resize(n);
    for(int  i = n; i > 0; i--){
        for(int j = 0; j < n; j++)
            used1[j] = false;
        for(int j = 0; j < n; j++)
            used2[j] = false;
        used2[ind] = true;
        dfs(ind, 0, i);
        int cnt = 0;
        for (int j = 0; j < n; j++)
            if(used2[j])
                cnt++;
        //for(int j = 0; j < n; j++)
            //cout << used2[j] << " ";
        //cout << endl;
        if (cnt >= k){
            cu = i;
            break;
        }
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
    //cout << u+1 << " " << w+1 << " ";
    int cur_ans = dist[u][w], res1 = 0, res2 = 0;
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
        //cout << ind + 1 << " ";
    }


    cout << max(cur_ans, cu);
}
