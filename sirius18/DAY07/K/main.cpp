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
vector<int> e[MAXN];
vector<int> used(MAXN, 0);
vector<int> used2(MAXN, 0);
vector<int> comp(MAXN, 0);
vector<int> tsort;
int ans = 0;
int n, m, x, y, cnt=1;

void dfs(int v){
    used[v] = 1;
    for(auto i : g[v])
        if(!used[i])
            dfs(i);
    tsort.pb(v);
}

void dfs2(int v){
    used2[v] = 1;
    comp[v] = cnt;
    for(auto i : e[v])
        if(!used2[i])
            dfs2(i);
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    //m = n;
    tsort.reserve(n);
    FJ{
        cin >> x >> y;
        x--;
        y--;
        g[x].pb(y);
        e[y].pb(x);
    }


    FI{
        //cout << i << ' ' << used[i] << '\n';
        if (!used[i])
            dfs(i);
    }

    reverse(tsort.begin(), tsort.end());
    for(auto i : tsort){
        if(!used2[i]){
            dfs2(i);
            cnt++;
        }
    }

    cout << cnt-1 << '\n';
    FI
        cout << comp[i] << ' ';

    return 0;
}
