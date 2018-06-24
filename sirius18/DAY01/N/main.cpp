#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <utility>
#include <functional>
#include <set>

#define mp make_pair
#define ll long long
#define FI for(int i;i<n;i++)
#define pb push_back

using namespace std;
vector<int> a;
int main() {
    ll INF = 10000000000000000;
	int n, m, s, f, w, b, e, c;
	cin >> n;
	vector<int> cost(n);
	//FI{
    //    cin >> c;
    //    cout << '1';
    //    cost.pb(c);
	//}
	cin >> m;
	vector< vector <pair<int, int> > > g(n);
	for (int i = 0; i < m; i++) {
            cin >> b >> e;
            b--;
            e--;
            pair<int, int> p1 = mp(e, cost[b]);
            g[b].pb(p1);
            pair<int, int> p2 = mp(b, cost[e]);
            g[e].pb(p2);
    }
    s=1;f=n;
	s--;
	f--;
    vector<ll> d (n, INF);
	d[s] = 0;
	set < pair<ll,int> > q;
	q.insert (mp (d[s], s));
	while (!q.empty()) {
		int v = q.begin()->second;
		q.erase(q.begin());

		for (size_t j=0; j<g[v].size(); ++j) {
			int to = g[v][j].first,
				len = g[v][j].second;
			if (d[v] + len < d[to]) {
				q.erase (mp (d[to], to));
				d[to] = d[v] + len;
				q.insert (mp (d[to], to));
			}
		}
	}
	if (d[f] == INF){
        cout << -1;
	}
	else{
        cout << d[f];
	}
	return 0;
}
