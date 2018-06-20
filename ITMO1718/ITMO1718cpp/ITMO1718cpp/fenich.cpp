#include <vector>
#include <string>
#include <iostream>

using namespace std;

vector<int> t;
int n;

void init(int nn)
{
	n = nn;
	t.assign(n, 0);
}

int sum(int r)
{
	int result = 0;
	for (; r >= 0; r = (r & (r + 1)) - 1)
		result += t[r];
	return result;
}

void inc(int i, int delta)
{
	for (; i < n; i = (i | (i + 1)))
		t[i] += delta;
}

int sum(int l, int r)
{
	return sum(r) - sum(l - 1);
}

void init(vector<int> a)
{
	init((int)a.size());
	for (unsigned i = 0; i < a.size(); i++)
		inc(i, a[i]);
}

int main() {
	string command;
	int num, res;
	int cnt = 0;

	t.resize(10 * 10 * 10 * 10 * 10);

	do {
		cin >> command;
		cin >> num;
		if (command == "?") {
			res = sum(0, num);
			cout << res;
		}
		else if(command == "+") {
			t.push_back(num);
			for (int i = cnt; i < n; i = (i | (i + 1))) {
				t[i] += num;
			}
			cnt++;
		}
	} while (command != "");

	return 0;
}