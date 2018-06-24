#include <bits/stdc++.h>
#include "ext/rope"
#include "ext/pb_ds/detail/standard_policies.hpp"
#include "ext/pb_ds/assoc_container.hpp"

#define mp make_pair
#define pb push_back
#define eb emplace_back
#define sz size
#define sf scanf
#define ff first
#define ss second
#define FI for(int i = 0; i<n; ++i)
#define FI1 for(int i = 1; i<n; ++i)
#define FJ for(int j = 0; j<m; ++j)
#define FJ1 for(int j = 1; j<m; ++j)


using namespace std;
using namespace __gnu_cxx;
using namespace __gnu_pbds;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef size_t st;
typedef double db;
typedef unsigned int ui;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;
const int MAXN = 20000;
vector<int> g[MAXN];
vector<int> used(MAXN, 0), ret(MAXN, 0), tin(MAXN, 0);
set<int> points;

int n, m, x, y, t=0, b = 0;

void dfs(int v, int p){
    used[v] = 1;
    ret[v] = tin[v] = t++;
    int cnt = 0;
    for(auto i : g[v]){
        if (i == p)
            continue;
        if(used[i])
            ret[v] = min(ret[v], tin[i]);
        else if (!used[i]){
            cnt++;
            dfs(i, v);
            ret[v] = min(ret[v], ret[i]);
            if (ret[i] >= tin[v] && p != -1)
                points.insert(v);
        }
    }
    if (p == -1 && cnt > 1)
        points.insert(v);
}


int dfs2(int v){
    if(v == y)
        return 0;
    used[v] = 1;
    for(auto i : g[v]){
        if (!used[i] && i != b)
            if (!dfs2(i))
                return 0;
    }
    return 1;
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    //m = n;
    FJ{
        cin >> x >> y;
        x--;
        y--;
        g[x].pb(y);
        g[y].pb(x);
    }


    FI{
        //cout << i << ' ' << used[i] << '\n';
        if (!used[i])
            dfs(i, -1);
    }

    int q, cnt;
    set<int> ans;
    //cin >> q;
    //for(int i=0; i<q; i++){
        cin >> x >> y;
        x--; y--;
        cnt = 0;
        //cout << x << ' ' << y << ' ' << dfs2(x) << ' ';
        b = -2;
        used.assign(MAXN, 0);
        if (dfs2(x)){
            cout << "0\n";
        }else {
        for(auto u : points){
            b = -2;
            if (u != x && u != y){
                used.assign(MAXN, 0);
                b = u;
                if(dfs2(x))
                    ans.insert(u);
            }
        }
        cout << ans.size() << '\n';
        for (auto i : ans)
            cout << i+1 << ' ';
    //}
    }
    return 0;
}
