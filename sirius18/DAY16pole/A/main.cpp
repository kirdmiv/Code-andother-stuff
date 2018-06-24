#include <bits/stdc++.h>
#include "ext/rope"
#include "ext/pb_ds/detail/standard_policies.hpp"
#include "ext/pb_ds/assoc_container.hpp"

#define np nullptr
#define mp make_pair
#define pb push_back
#define eb emplace_back
#define sz size
#define sf scanf
#define ff first
#define ss second
#define FI for(int i = 0; i<n; ++i)
#define FI1 for(int i = 1; i<n; ++i)
#define FJ for(int j = 0; j<m; ++j)
#define FJ1 for(int j = 1; j<m; ++j)


using namespace std;
using namespace __gnu_cxx;
using namespace __gnu_pbds;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef size_t st;
typedef double db;
typedef unsigned int ui;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

const int INF = 1e9;
const int MAXN = 1002;

ll n, b, f, x;




int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> b >> f;
    vector<ll> a;
    FI{
        cin >> x;
        a.pb(x);
    }

    ll cnt = 0;
    ll it = 0;
    stable_sort(a.begin(), a.end());
    ll cur = 0;
    while (it < n){
        stable_sort(a.begin(), a.end());
        cnt += b;
        //cout << cur << '\n';
        cnt += a[it] - cur;
        cur = a[it] + b;
        it++;
        for(int i = it; i<n; ++i){
            while (a[i] < cur)
                a[i] += f;

        }
    }

    cout << cnt << '\n';

    return 0;
}
