#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <utility>
#include <functional>
#include <set>
#include <string>
#include <math.h>
#include <cmath>

#define mp make_pair
#define ff first
#define ss second
#define ll long long
#define pb push_back

using namespace std;

struct point {
	ll x, y;
};

double scalar(point a, point b) {
    return a.x * b.x + a.y * b.y;
}

double vectr(point a, point b) {
    return a.x * b.y - a.y * b.x;
}

double angle(point a, point b) {
    return atan2(vectr(a, b), scalar(a, b));
}

bool cmp (point a, point b) {
	return a.x < b.x || a.x == b.x && a.y < b.y;
}

bool cw (point a, point b, point c) {
	return a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y) < 0;
}

bool ccw (point a, point b, point c) {
	return a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y) > 0;
}

void obolochka (vector<point> & a) {
	if (a.size() == 1)  return;

	sort (a.begin(), a.end(), &cmp);
	point p1 = a[0],  p2 = a.back();
	vector<point> up, down;
	up.push_back (p1);
	down.push_back (p1);

	for (size_t i=1; i<a.size(); ++i) {
		if (i==a.size()-1 || cw (p1, a[i], p2)) {
			while (up.size()>=2 && !cw (up[up.size()-2], up[up.size()-1], a[i]))
				up.pop_back();
			up.push_back (a[i]);
		}
		if (i==a.size()-1 || ccw (p1, a[i], p2)) {
			while (down.size()>=2 && !ccw (down[down.size()-2], down[down.size()-1], a[i]))
				down.pop_back();
			down.push_back (a[i]);
		}
	}

	a.clear();
	for (size_t i=0; i<up.size(); i++)
		a.push_back (up[i]);
	for (size_t i=down.size()-2; i>0; i--)
		a.push_back (down[i]);
}

int main()
{
    const double PI = 3.14159265358979323846;
    vector <point> a;
    int n;
    ll x, y;
    point p;
    cin >> n;
    for (size_t i = 0; i < n; i++){
        cin >> x >> y;
        p.x = x;
        p.y = y;
        a.emplace_back(p);
    }
    obolochka(a);
    cout << a.size() << endl;
    for (size_t i = 0; i<a.size(); i++){
        cout << a[i].x << " " << a[i].y << endl;
    }
    return 0;
}
