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

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m, k, x, y;
    cin >> n >> m;

    vector<int> g[n];
    vector<int> e[n];

    FJ{
        cin >> x >> y;
        x--; y--;
        g[x].pb(y);
        e[y].pb(x);
    }

    deque<int> q;
    vector<int> d(n, INF);
    //vector<int> used(n, 0);
    cin >> k;
    for(int j = 0; j<k; j++){
        cin >> x >> y;
        //used.assign(n, 0);
        d.assign(n, INF);
        x--; y--;
        q.pb(x);
        d[x] = 0;
        //used[x] = 1;
        while (!q.empty()){
            //cerr << x << ' ';
            x = q.front();
            q.pop_front();
            for(auto i : g[x]){
                if (d[i] > d[x]){
                q.push_front(i);
                d[i] = d[x];
                //used[i] = 1;
                }
            }
            for(auto i : e[x]){
                if (d[i] > d[x] + 1){
                q.push_back(i);
                d[i] = d[x] + 1;
                //used[i] = 1;
                }
            }
        }
        //for(i : d)
        //    cout << i << ' ';
        //cout << '\n';
        if (d[y] == INF)
            cout << -1 << '\n';
        else
            cout << d[y] << '\n';
    }

    return 0;
}
