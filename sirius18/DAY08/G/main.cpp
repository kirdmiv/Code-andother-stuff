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

struct edge{
    int b, e, c;
    edge(int ak, int bk, int co) : b(ak), e(bk), c(co){}
};


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m, k, s, f, a, b, c;
    cin >> n >> m >> k >> s >> f;
    s--; f--;

    vector< vector<int> >g(n, vector<int> (n, INF));

    FJ{
        cin >> a >> b >> c;
        a--; b--;
        g[a][b] = min(g[a][b], c);
    }

    vector<edge> e;

    m = n;
    FI{
        FJ{
            if(g[i][j] != INF)
                e.eb(edge(i, j, g[i][j]));
        }
    }

    vector< vector<int> > d(n, vector<int> (k+1, INF));
    d[s][0] = 0;
    for(int i= 1; i<k+1; i++){
        for(auto ed : e){
                //cerr << ed.b << ' ' << ed.e << ' ' << ed.c <<' ' << '\n';
            if(d[ed.b][i-1] < INF){
                //d[ed.e][i] = min(d[ed.e][i], d[ed.b][i] + ed.c);
                                    //cerr << ed.b << ' ' << ed.e << ' ' << ed.c <<' ' << '\n';
                //if (i > 0){
                    d[ed.e][i] = min(d[ed.e][i], d[ed.b][i-1] + ed.c);
                    d[ed.e][i] = min(d[ed.e][i], d[ed.e][i-1]);
                //}
                //cout << ed.e << ' ' << d[ed.e][i] << '\n';
            }
        }
    }

    if (d[f][k] < INF)
        cout << d[f][k] << '\n';
    else
        cout << -1 << '\n';
    return 0;
}
