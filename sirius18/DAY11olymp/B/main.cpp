#include <bits/stdc++.h>
#include "ext/rope"
#include "ext/pb_ds/detail/standard_policies.hpp"
#include "ext/pb_ds/assoc_container.hpp"

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

    ll x, mins=0, minns=0, minss=0;
    while (1){
        cin >> x;
        if (x == 0){
            if((mins != 0 && minns != 0)){
                cout << mins * minns;
                return 0;
            }
            //if((minss != 0 && mins != 0)){
            //    cout << mins * minss;
            //    return 0;
            //}
            cout << 1;
            return 0;
        }
        if (x%49 != 0){
            if (x %7 == 0)
                mins = max(mins, x);
            else
                minns = max(minns, x);
        } //else
            //minss = max(minss, x);
    }


    return 0;
}
