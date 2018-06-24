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
const int MAXN = 100000;
vector<int> g[MAXN];
vector<int> used(MAXN, false);
vector<int> ans[MAXN];
vector<int> comp(MAXN, 0);
int n, m, b, e, cnt = 0;

void dfs(int v){
    used[v] = 1;
    ans[cnt].pb(v);
    comp[v] = cnt;
    for(auto i : g[v]) if(!used[i]) dfs(i);
    //used[v] = 2;
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    FJ{
        cin >> b >> e;
        b--;
        e--;
        g[b].pb(e);
        g[e].pb(b);
    }

    FI{
        //cout << i << ' ' << used[i] << '\n';
        if (!used[i]){
            dfs(i);
            cnt++;
        }
    }

    int q, a, b;
    cin >> q;
    for(int i =0; i<q; i++){
        cin >> a >> b;
    a--;b--;
        if(comp[a] == comp[b])
            cout << ans[comp[a]].size() << '\n';
        else
            cout << 0 << '\n';
    }

    return 0;
}
