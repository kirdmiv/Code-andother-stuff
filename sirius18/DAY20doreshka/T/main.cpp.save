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
const int MAXN = 100;

int n, s, x, k, v;
vector<int> g[MAXN];
vector<int> p(MAXN, -1);
vector<int> used(MAXN, -1);


int dfs(int v){
    used[v] = k;
    for(int i = 0; i<n; ++i){
        if(g[i][v] && p[i] == -1){
            p[i] = v;
            return 1;
        }
    }
    for(int i = 0; i<n; ++i){
        if(g[i][v] && !(used[i]==k) && dfs(p[i])){
            p[i] = v;
            return 1;
        }
    }
    return 0;
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> v;
    int m = n;
    s = n;

    int x, y;
    vector<int> t(n, -1);
    FI{
        cin >> st >> x >> y;
        int ch = stoi(st[0] + st[1]);
        int mi = stoi(st[3] + st[4]);

    }

    int ans = 0;
    for(k=0; k<s; k++){
        ans += dfs(k);
    }

    cout << ans;
    return 0;
}
