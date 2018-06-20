#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <utility>
#include <functional>
using namespace std;
vector<int> a;
int main() {
    long long INF = 10000000000000000;
	int n, s, f, k;
	ifstream fin;
	fin.open("pathmgep.in");
	ofstream fout;
	fout.open("pathmgep.out");
	fin >> n >> s >> f;
	vector< vector <pair<int, int> > > g(n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
            fin >> k;
            if (k != -1){
                pair<int, int> p = make_pair(j, k);
                g[i].push_back(p);
            }
		}
	}
	s--;
	f--;
    vector<long long> d (n, INF),  p (n);
	d[s] = 0;
	vector<char> u (n);
	while (true) {
		int v = -1;
		for (int j=0; j<n; ++j)
			if (!u[j] && (v == -1 || d[j] < d[v]))
				v = j;
		if (v == -1)
			break;
		u[v] = true;

		for (size_t j=0; j<g[v].size(); ++j) {
			int to = g[v][j].first,
                w = g[v][j].second;
			if (d[v] + w < d[to]) {
				d[to] = d[v] + w;
				p[to] = v;
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
