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
#include <queue>

#define mp make_pair
#define ff first
#define ss second
#define ll long long
#define pb push_back
#define st size_t
#define FI for(int i = 0; i < n; i++)

using namespace std;
int n;
vector< pair<int, int> > p;
//inline int mn(int x, int y){
//    return y + ((x - y) & ((x - y) >> (sizeof(int) * CHAR_BIT - 1))); // min(x, y)
//}
//inline int mx(int x, int y){
//    return x - ((x - y) & ((x - y) >> (sizeof(int) * CHAR_BIT - 1))); // max(x, y)
//}

int main(){
    int x, y;
    cin >> n;
    n --;
    cin >> x >> y;
    p.pb(mp(x, y));
    int mxx, mnx;
    mxx = mnx = x;
    int mxy, mny;
    mxy = mny = y;
    FI{
        cin >> x >> y;
        p.pb(mp(x, y));
        mxx = max(mxx, x);
        mnx = min(mnx, x);
        mxy = max(mxy, y);
        mny = min(mny, y);
    }
    double x0 = (double)(mxx-mnx)/2;
    double y0 = (double)(mxy-mny)/2;
    cout << (double)(mxx-mnx)/2 << " " << (double)(mxy-mny)/2 << '\n';
    double mxd = 0;
    n++;
    FI{
        mxd = max(mxd, sqrt((x0 - p[i].ff) * (x0 - p[i].ff) + (y0 - p[i].ss) * (y0 - p[i].ss)));
    }
    cout << fixed << mxd;
    return 0;
}
