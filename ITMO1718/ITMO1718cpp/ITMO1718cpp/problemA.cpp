#include <iostream>
#include <vector>
using namespace std;

int main() {
	vector<int> parents;
	int n;
	cin >> n;
	int tmp;
	for (int i = 0; i < n; ++i) {
		cin >> tmp;
		parents.emplace_back(tmp);
	}
	int m;
	cin >> m;
	bool flag;
	int a, b;
	for (int i = 0; i < m; ++i) {
		cin >> a, b;
		flag = false;
		while (parents[b - 1] != 0) {
			if (a == b) {
				cout << 1;
				flag = true;
				break;
			};
			b = parents[b - 1];
			if ((!flag) & (parents[a - 1] != 0)) {
				cout << 0;
			};
			if (parents[a - 1] == 0) {
				cout << 1;
			}

		}
	}
	return 0;
}