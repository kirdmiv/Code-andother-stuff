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
vector<int> p;
vector<int> ans;
vector<int> tsort;
int n, m, b, e, x;
ll cnt=0;

void dfs(int v){
    used[v] = 1;
    //ans.pb(v);
    //cnt += p[v];
    for(auto i : g[v]){
        if(!used[i]){
            dfs(i);
        }
    }
    tsort.pb(v);
    //used[v] = 2;
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;

    FI{
        cin >> x;
        p.pb(x);
    }
    FI{
        cin >> x;
        for(int j=0; j<x;j++){
            cin >> e;
            e--;
            g[i].pb(e);
        }
    }

    dfs(0);
    cnt = 0;
    for(int i =0; i<tsort.size(); i++){
        cnt += (ll)p[tsort[i]];
    }
    //reverse(ans.begin(), ans.end());
    cout << cnt << ' ' << tsort.size() << '\n';
    for(int i = 0; i < tsort.size(); i++)
        cout << tsort[i]+1 << ' ';

    return 0;
}
