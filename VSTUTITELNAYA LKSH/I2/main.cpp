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
int n, ind;
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
    int c = cur;
    if (v == ind)
        c = 0;
    //cout << cur << " " << v << " " << ind << endl;

    for(int i = 0; i < g[v].size(); i++){
        cur = min(cur, dfs(g[v][i], c+1, dist));
        c = cur;
    }
    if(cur >= dist){
        used2[v] = true;
        //cout << cur << " " << v << " " << ind << endl;

        return 1;
    }
    //cout << cur << " " << v << " " << ind << endl;
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
    int mx = 0;
    for (int i = 0; i < n; i ++){
        if (d[i] > d[ind]){
            ind = i;
            mx = d[i];
        }
    }
    used1.resize(n);
    used2.resize(n);
    for(int  i = n; i > 0; i--){
        for(int j = 0; j < n; j++)
            used1[j] = false;
        for(int j = 0; j < n; j++)
            used2[j] = false;
        used2[ind] = true;
        dfs(ind, i, i);
        int cnt = 0;
        for (int j = 0; j < n; j++)
            if(used2[j])
                cnt++;
        //for(int j = 0; j < n; j++)
            //cout << used2[j] << " ";
        //cout << endl;
        if (cnt >= k){
            cout << i;
            return 0;
        }
    }
}
