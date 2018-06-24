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


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m, x;
    cin >> n;
    m = n;
    vector<int> a[n];
    FI{
        FJ{
            cin >> x;
            a[i].pb(x);
        }
    }
    string ans = "YES";
    FI{
        FJ{
            if(a[i][j]){
                for(int k=0; k<n; k++){
                    if(a[j][k] == 1 && a[i][k] != 1)
                        ans = "NO";
                }
            }
        }
    }
    cout << ans;
    return 0;
}
