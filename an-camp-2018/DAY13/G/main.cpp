#include "bits/stdc++.h"
#define puba push_back
#define ff first
#define ss second
#define bend(_x) begin(_x), end(_x)
#define szof(_x) ((int) (_x).size())


using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int INF = 1e9 + 7;
const double PI = atan2(0, -1);

struct point {
    int x, y;
    point() {
        x = y = 0;
    }
    point(int _x, int _y) {
        x = _x;
        y = _y;
    }
    ll operator*(point p) {
        return (ll) x * p.y - (ll) y * p.x;
    }
    point operator-(point p) {
        return point(x - p.x, y - p.y);
    }
    point operator+(point p) {
        return point(x + p.x, y + p.y);
    }
};

int main() {
    int n;
    ll v;
    scanf("%d%lld", &n, &v);
    ll sum = 0;

    for (int i = 0; i < n; ++i) {
        int k;
        scanf("%d", &k);

        ll now = 0;
        vector<point> inp;
        for (int j = 0; j < k; ++j) {
            int x, y;
            scanf("%d%d", &x, &y);
            inp.puba(point(x, y));
        }
        for (int j = 0; j < k; ++j) {
            int next = (j + 1) % k;
            now += inp[j] * inp[next];
        }
        sum += abs(now);
    }

    printf("%.8f\n", v / (double) sum * 2);
    return 0;
}
