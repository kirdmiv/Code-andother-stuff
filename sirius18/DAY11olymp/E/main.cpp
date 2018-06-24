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
const int MAXN = 2000;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m, x, a, b;
    ui maxst=0;
    deque<int> q;
    cin >> n;
    vector<int> d(n, INF);
    vector<int> d2(n, 0);
    vector<int> g[n];
    set<int> e, ne;

    for(int i=0; i<n; i++){
        cin >> x;
        if(x){
            q.pb(x);
            d[x] = 0;
            d2[0]++;
            maxst++;
            //e.insert(i);
        }
    }

    cin >> m;

    FJ{
        cin >> a >> b;
        a--; b--;
        g[a].eb(b);
        g[b].eb(a);
    }

    while(!q.empty()){
        x = q.front();
        q.pop_front();
        for(auto i : g[x]){
            if(e.count(i) == 0 && (d[x]+1)%2==0){
                e.insert(i);
                q.pb(i);
            }
            if(ne.count(i) == 0 && (d[x]+1)%2==1){
                ne.insert(i);
                q.pb(i);
            }
            if(d[i] > d[x]+1){
                d[i] = d[x]+1;
                q.pb(i);
                d2[d[x]+1]++;
            }
        }
    }
    cout << max(max(e.size(), ne.size()), maxst);
    return 0;
}
