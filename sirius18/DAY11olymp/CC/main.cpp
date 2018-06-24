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

vector< vector<int> > g(MAXN, vector<int> (MAXN, 0));

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m, a, b;
    cin >> n >> m;

    FJ{
        cin >>a >> b;
        a--; b--;
        g[a][b] = 1;
        g[b][a] = 1;
    }

    ll res = 1, ans = 0;
    for (int i=0; i<n;i++){
        res *= 2;
    }
    //bitset<32> bs;
    for(ll i=0; i<res; i++){
        bitset<32> bs;
        ll m = i;
        for (int z = 0; z<n; z++){
            int bt = (m >> z) & 1;
            //cout << bt << ' ';
            if (bt)
                bs.set(z);
        }
        //bs.set(i);
        bool f = true;
        for(int k=0; k<n; k++){
            for(int j=0; j<n; j++){
                if(g[k][j] && bs.test(k) && bs.test(j))
                    f = false;
            }
        }
        if (f)
            ans++;
    }

    cout << ans;
    return 0;
}
