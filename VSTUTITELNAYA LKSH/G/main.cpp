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
	double x, y;
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
    double x, y, x1, x2, x3, y1, y2, y3;
    point p;
    cin >> n;
    for (size_t i = 0; i < n; i++){
        cin >> x >> y;
        p.x = x;
        p.y = y;
        a.emplace_back(p);
    }
    obolochka(a);
    size_t sz = a.size();
    point p1, p2;
    double ans, res;
    ans = 180;
    for(size_t i = 0; i < a.size(); i++){
        x1 = a[i].x;
        x2 = a[(i+1)%sz].x;
        x3 = a[(i+2)%sz].x;

        y1 = a[i].y;
        y2 = a[(i+1)%sz].y;
        y3 = a[(i+2)%sz].y;

        p1.x = x1 - x2;
        p2.x = x3 - x2;

        p1.y = y1 - y2;
        p2.y = y3 - y2;

        res = abs(angle(p1, p2) / PI * 180);
        ans = min(ans, res);
        //cout << x1 << " " << y1 << " " << res << endl;
    }
    cout << ans;
    return 0;
}
