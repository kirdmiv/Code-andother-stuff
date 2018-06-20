#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <utility>
#include <functional>
#include <set>

#define mp make_pair
#define ff first
#define ss second

using namespace std;
vector<int> a;
int main() {
    long long INF = 10000000000000000;
	int n, m, nn, s, f, w, b, e, A, B;
	cin >> n >> nn;
	cin >> s >> f;
	vector< vector <pair<int, int> > > g(n);
	for (int i = 0; i < nn; i++) {
            cin >> b >> e >> w;
            b--;
            e--;
            pair<int, int> p1 = mp(e, w);
            g[b].push_back(p1);
            pair<int, int> p2 = mp(b, w);
            g[e].push_back(p2);
    }
    cin >> A >> B;

	s--;
	f--;
    vector<long long> d_a (n, INF);
	vector<long long> d_b (n, INF);
	d_a[s] = 0;
	set < pair<int,int> > q;
	q.insert (mp (0, s));

	while (!q.empty()) {
		int v = q.begin()->ss;
		int sm = q.begin()->ff;
		q.erase(q.begin());

		for (size_t j=0; j<g[v].size(); j++) {
			int to = g[v][j].ff,
				len = g[v][j].ss;
			m = sm;
			if (m == 0){
                if (d_a[v] + len < d_a[to] && len <= A){
                    d_a[to] = d_a[v] + len;
                    q.insert(mp(m, to));
                }
                if (d_a[v] + len < d_b[to] && len >= B){
                    m = 1;
                    d_b[to] = d_a[v] + len;
                    q.insert(mp(m, to));
                }
			}
			if (m == 1){
                if (d_b[v] + len < d_b[to] && len >= B){
                    m = 1;
                    d_b[to] = d_b[v] + len;
                    q.insert(mp(m, to));
                }
			}
			/*if (d[v] + len < d[to] || (d[v] + len == d[to] && m == 0)) {
                if (m == 0 && len <= A){
                    m = 0;
                    //cout << v+1 << " " << to+1 << " ";
                }
                else if (m == 0 && len >= B)
                    m = 1;
                else if (m == 1 && len >= B)
                    m = 1;
                else
                    continue;
				q.erase(mp(m, to));
				d[to] = d[v] + len;
				q.insert(mp(m, to));
            //cout << j << " ";
			}*/
		}
	}

    long long ans = min(d_a[f], d_b[f]);
	if (ans == INF){
        cout << -1;
	}
	else{
        cout << ans;
	}
	return 0;
}
