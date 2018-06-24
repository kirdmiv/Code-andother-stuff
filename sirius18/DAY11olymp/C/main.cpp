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

const int INF = 1e9;
const int MAXN = 21;

vector<int> g[MAXN];
vector<int> used(0, MAXN);
vector<int> res;
int cnt;

void dfs(int v){
    used[v] = 1;
    cnt += 1;
    for(auto i : g[v])
        if(!used[i])
            dfs(i);
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    ll s[] = {2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576};
    int n, m, a, b;
    cin >> n >> m;
    FJ{
        cin >> a >> b;
        a--; b--;
        g[a].eb(b);
        g[b].eb(a);
    }

    FI{
        cnt = 0;
        if(!used[i]){
            dfs(i);
            res.eb(cnt);
        }
    }
    ull ans = 1;
    for(auto i : res){
        ans *= s[i];
    }
    cout << ans;
    return 0;
}
