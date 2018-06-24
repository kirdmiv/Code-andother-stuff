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
const int MAXN = 1e6+1;

//vector<int> g[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, u, c1, c2, c3, m, k, x;
    cin >> n >> u >> c1 >> c2 >> c3 >> m;

    vector<int> lol;
    vector< vector <pair<int, int> > > g(MAXN);
    FJ{
        cin >> k;
        for(int i=0; i<k; ++i){
            cin >> x;
            x--;
            lol.pb(x);
        }
        int mx, mn, mx1, mx2, mn1, mn2;
        for(auto x : lol){
            for(auto y : lol){
                g[x].eb(mp(y, c2+c3));
                g[y].eb(mp(x, c2+c3));
                mx = max(x, y);
                mn = min(x, y);
                g[mx].eb(mp(mn, (mx-mn)*c1));
                g[mn].eb(mp(mx, (mx-mn)*u));

                g[0].eb(mp(mn, (mn)*u));
                g[mn].eb(mp(0, (mn)*c1));

                g[0].eb(mp(mx, (mx)*u));
                g[mx].eb(mp(0, (mx)*c1));

                mx1 = max(mx, n);
                mn1 = min(mx, n);
                g[mx1].eb(mp(mn1, (mx1-mn1)*c1));
                g[mn1].eb(mp(mx1, (mx1-mn1)*u));

                mx2 = max(mn, n);
                mn2 = min(mn, n);
                g[mx2].eb(mp(mn2, (mx2-mn2)*c1));
                g[mn2].eb(mp(mx2, (mx2-mn2)*u));

            }
        }
        lol.clear();
    }

    //for(int r=1; r<MAXN; r++){
    //    g[r-1].eb(mp(r, u));
    //    g[r].eb(mp(r-1, c1));

    //}

    int s = 1, f = n;

    s--;
	f--;
    vector<int> d (MAXN, INF);
	d[s] = 0;
	set < pair<int,int> > q;
	q.insert (make_pair (d[s], s));
	//cerr << "ok";
	while (!q.empty()) {
		int v = q.begin()->second;
		q.erase(q.begin());

		for (st j=0; j<g[v].size(); ++j) {
			int to = g[v][j].ff,
				len = g[v][j].ss;
			if (d[v] + len < d[to]) {
				q.erase (mp (d[to], to));
				d[to] = d[v] + len;
				q.insert (mp (d[to], to));
			}
		}
		//cerr << "FUCK ";
	}

    cout << d[f];
    return 0;
}
