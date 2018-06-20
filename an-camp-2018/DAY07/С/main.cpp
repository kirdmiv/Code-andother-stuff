#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <utility>
#include <functional>
#include <set>
using namespace std;
vector<int> a;
int main() {
    long long INF = 10000000000000000;
	int n, m, s, f, w, b, e;
	ifstream fin;
	fin.open("distance.in");
	ofstream fout;
	fout.open("distance.out");
	fin >> n >> m;
	fin >> s >> f;
	vector< vector <pair<int, int> > > g(n);
	for (int i = 0; i < m; i++) {
            fin >> b >> e >> w;
            b--;
            e--;
            pair<int, int> p1 = make_pair(e, w);
            g[b].push_back(p1);
            pair<int, int> p2 = make_pair(b, w);
            g[e].push_back(p2);
    }
	s--;
	f--;
    vector<long long> d (n, INF);
	d[s] = 0;
	set < pair<long long,int> > q;
	q.insert (make_pair (d[s], s));
	while (!q.empty()) {
		int v = q.begin()->second;
		q.erase(q.begin());

		for (size_t j=0; j<g[v].size(); ++j) {
			int to = g[v][j].first,
				len = g[v][j].second;
			if (d[v] + len < d[to]) {
				q.erase (make_pair (d[to], to));
				d[to] = d[v] + len;
				q.insert (make_pair (d[to], to));
			}
		}
	}
	if (d[f] == INF){
        fout << -1;
	}
	else{
        fout << d[f];
	}
	fin.close();
	fout.close();
	return 0;
}
