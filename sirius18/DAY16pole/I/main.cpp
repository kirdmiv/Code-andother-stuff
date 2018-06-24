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
const int MAXN = 100;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    ull a, b;
    cin >> a >> b;
    ull cnt =0;
    for(ull i = a; i < b+1; i++){
        string k = to_string(i);
        ull g = 0;
        for (ll j=0; j<k.size(); j++){
            g += k[j] - '0';
        }
        if (g % 2 == 0)
            cnt++;
    }
    cout << cnt << '\n';
    return 0;
}
