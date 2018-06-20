#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <utility>
#include <functional>
#include <set>
#include <string>

#define mp make_pair
#define ff first
#define ss second
#define ll long long
#define pb push_back

using namespace std;
const int MAXN = 100000;
vector <long long> t(4*MAXN, 0);
vector <long long> delta(4*MAXN, -1);
int n, k;
// int last = 1;
int sum (int v, int tl, int tr, int l, int r, int x) {
    if (tl > r || tr < l) return 0;
    //cout << tl << ' ' << tr << ' ' << l << ' ' << r << '\n';
    if (l <= tl && tr <= r) {
        if (x != -1){
            t[v] = x * (tr - tl + 1);
            //cout << x << ' ' << t[v] << '\n';
            delta[v] = x;
        }
        else
            //cout << x << ' ' << t[v] << '\n';
            delta[v] = -1;
        return t[v];
    }
    int m = (tl + tr) / 2;
    if (delta[v] != -1){
        t[2 * v] = delta[v] * (m - tl + 1);
        t[2 * v + 1] = delta[v] * (tr - m);
        delta[2 * v] = delta[2 * v + 1] = delta[v];
        delta[v] = -1;
    }
    int ans = sum(2 * v, tl, m, l, r, x) + sum(2 * v + 1, m + 1, tr, l, r, x);
    ll tmp = 0;
    if (2 * v >= n)
        tmp += t[2 * v];
    if (2 * v + 1 >= n)
        tmp += t[2 * v + 1];
    t[v] = tmp;
    return ans;
}

int main()
{
    cin >> n >> k;
    int power = 0;
    while ((1 << power) < n) power++;
    int N = (1 << power);
    // cout << last << '\n';
    char mode;
    int l, r, x;
    for (int i = 0; i < k; i++){
        cin >> mode >> l >> r;
        if (mode == 'A'){
            cin >> x;
            sum(1, 1, N, l, r, x);
        }
        else
            cout << sum(1, 1, N, l, r, -1) << '\n';
        // for (int i = 1;i <= last;i++) cout <<t[i] << ' ';
        // cout << '\n';
    }
    return 0;
}
