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

    int n, x;
    vector<int> a;
    bool f;

    cin >> n;
    a.reserve(n);
    FI{
        cin >> x;
        a.eb(x);
    }

    vector< vector<int> > dp(n+1, vector<int> (n, INF));

    FI{
        dp[1][i] = 0;
    }

    for(int i =2; i<n+1; i++){
        for(int k=0; k<n-i+1; ++k){
            f = true;
            for(int j = k+1; j < k+i-1; ++j){
                if(a[j-1] > a[j])
                    f = false;
            }

            if (f){
                dp[i][k] = 0;
                continue;
            }

            for(int j= k; j<k+i-1; j++){
                dp[i][k] = min(dp[i][k], dp[j+1][0] + dp[i-j-1][j+1]);
            }

        }
    }

    cout << dp[n][0] << '\n';
    return 0;
}
