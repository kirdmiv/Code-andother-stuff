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
const int MAXN = 100;
vector<int> a[MAXN];
vector<int> used(MAXN, 0);
vector<int> tsort;
int ans = 0;
int n, m, x, y;

void dfs(int v){
    used[v] = 1;
    if (ans)
        return;
    for(auto i : a[v]){
        if(!used[i])
            dfs(i);
        else if (used[i] == 1){
            ans = 1;
            return;
        }
    }
    tsort.pb(v);
    used[v] = 2;
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
        a[x].pb(y);
    }


    FI{
        //cout << i << ' ' << used[i] << '\n';
        if (!used[i])
            dfs(i);
    }

    if(!ans){
        reverse(tsort.begin(), tsort.end());
        cout << "Yes" << '\n';
        for(auto i : tsort)
            cout << i+1 << ' ';
    } else
        cout << "No";
    return 0;
}
