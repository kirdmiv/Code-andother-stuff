#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <utility>
#include <functional>
using namespace std;
int main() {
	int n;
	ifstream fin;
	fin.open("floyd.in");
	ofstream fout;
	fout.open("floyd.out");
	fin >> n;
	vector< vector<int> > g(n, vector<int>(n, 0));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
            fin >> g[i][j];
		}
	}
	for (int k = 0; k < n; k++){
        for (int v = 0; v < n; v++){
            for (int u = 0; u < n; u++){
                g[v][u] = min(g[v][u], g[v][k] + g[k][u]);
            }
        }
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
            fout << g[i][j] << " ";
		}
		fout << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
