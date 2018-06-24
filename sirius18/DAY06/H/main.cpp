#define _GLIBCXX_DEBUG
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
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);

    vector<int> ans;
    int n, k, cnt;
    int cn;
    cin >> n >> k;
    cn = n;
    vector<bool> used(n+1, false);
    vector<ll> fact(n+1, 1);
    fact[0] = 1;
    for(int i = 1; i<n+1; ++i){
        fact[i] = fact[i-1] * i;
    }
    k-=1;
    while (n > 0){
        n-=1;
        cnt = fact[n];
        //cout << "loll";
        for(int i=1; i<cn+1;i++){
            //cout << cnt << ' ' << k << '\n';

            if (k >= cnt && !used[i])
                k -= cnt;
            else if (k < cnt && !used[i]){
                //cout << "lol";
                ans.pb(i);
                used[i] = true;
                break;
            }
        }
    }
    //cout << ans.size() << '\n';
    for(int i = 0; i<ans.size(); ++i){
        cout << ans[i] << ' ';
    }
    return 0;
}
