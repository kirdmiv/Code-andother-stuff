#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <utility>
#include <functional>
using namespace std;

struct Edge {
	int b, e, cost;
};

int main() {
    int INF = 1000000000;
	int n, m, w, b, e;
	cin >> n >> m;
	vector<Edge> edges(m);
	vector< vector <pair<int, int> > > g(n);
	for (int i = 0; i < m; i++) {
            cin >> b >> e >> w;
            Edge edge;
            b--;
            e--;
            edge.b = b;
            edge.e = e;
            edge.cost = w;
            edges[i] = edge;
	}

    vector<int> d (n, INF);
	d[0] = 0;
	int x;
	for (int i=0; i<n; ++i) {
		x = -1;
		for (int j=0; j<m; ++j)
			if (d[edges[j].b] < INF)
				if (d[edges[j].e] > d[edges[j].b] + edges[j].cost) {
					d[edges[j].e] = max (-INF, d[edges[j].b] + edges[j].cost);
					x = edges[j].e;
				}
	}

	if (x != -1)
		fout << "yes";
    else
        fout << "no";
	return 0;
}
