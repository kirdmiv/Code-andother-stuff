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
int n, m, b, e, cnt = 0;

void dfs(int v){
    used[v] = 1;
    ans[cnt].pb(v);
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

    cout << cnt << '\n';
    for(int i=0; i<cnt; i++){
        cout << ans[i].size() << '\n';
        for(int j=0; j<ans[i].size(); j++){
            cout << ans[i][j]+1 << ' ';
        }
        cout << '\n';
    }
    return 0;
}
