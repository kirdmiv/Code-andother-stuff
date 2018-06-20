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
int n, l;
inline int mn(int x, int y){
    return y + ((x - y) & ((x - y) >> (sizeof(int) * CHAR_BIT - 1))); // min(x, y)
}
inline int mx(int x, int y){
    return x - ((x - y) & ((x - y) >> (sizeof(int) * CHAR_BIT - 1))); // max(x, y)
}

int main(){
    int x1, y1, x0, y0, x2, y2;
    cin >> n >> l;
    n--;
    cin >> x0 >> y0;
    x1 = x0;
    x2 = y0;
    double ans = 0;
    FI{
        cin >> x2 >> y2;
        ans += sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
        x1 = x2;
        y1 = y2;
    }
    ans += sqrt((x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0));
    //ans += l * n;
    cout << ans;
    return 0;
}
