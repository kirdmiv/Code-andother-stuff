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
const int MAXN = 10000;

int n, v;
vector< pair<int, int> > a;
vector< int> b(MAXN, 0);
vector < pair<int, int> > dp(MAXN, mp(INF, INF));







/*
░░░░░░░░░
░░░░▄▀▀▀▀▀█▀▄▄▄▄░░░░
░░▄▀▒▓▒▓▓▒▓▒▒▓▒▓▀▄░░
▄▀▒▒▓▒▓▒▒▓▒▓▒▓▓▒▒▓█░
█▓▒▓▒▓▒▓▓▓░░░░░░▓▓█░
█▓▓▓▓▓▒▓▒░░░░░░░░▓█░
▓▓▓▓▓▒░░░░░░░░░░░░█░
▓▓▓▓░░░░▄▄▄▄░░░▄█▄▀░
░▀▄▓░░▒▀▓▓▒▒░░█▓▒▒░░
▀▄░░░░░░░░░░░░▀▄▒▒█░
░▀░▀░░░░░▒▒▀▄▄▒▀▒▒█░
░░▀░░░░░░▒▄▄▒▄▄▄▒▒█░
░░░▀▄▄▒▒░░░░▀▀▒▒▄▀░░
░░░░░▀█▄▒▒░░░░▒▄▀░░░
░░░░░░░░▀▀█▄▄▄▄▀ Kappa

*/












void dfs(int v){
    if (v >= (n+1)/2){
        if (b[v] == 0)
            dp[v].ff = 0;
        else
            dp[v].ss = 0;
        return;
    }

    dfs(2*v);
    dfs(2*v+1);

    //if (a[v-1].ss != 1){
        if (a[v-1].ff == 1){
            dp[v].ss = min(dp[v].ss, dp[2*v].ss + dp[2*v+1].ss);
            dp[v].ff = min(dp[v].ff, min(min(dp[2*v].ff + dp[2*v+1].ff, dp[2*v].ss + dp[2*v+1].ff), dp[2*v].ff + dp[2*v+1].ss));
        }
        else{
            dp[v].ss = min(dp[v].ss, min(min(dp[2*v].ss + dp[2*v+1].ff, dp[2*v+1].ss + dp[2*v].ff), dp[2*v+1].ss + dp[2*v].ss));
            dp[v].ff = min(dp[v].ff, dp[2*v].ff + dp[2*v+1].ff);
        }
    //}
    if(a[v-1].ss == 1){
        if (a[v-1].ff == 1){
            dp[v].ss = min(dp[v].ss, min(dp[2*v].ss + dp[2*v+1].ff + 1, dp[2*v+1].ss + dp[2*v].ff + 1));
        }
        else{
            dp[v].ff = min(dp[v].ff, min(dp[2*v].ss + dp[2*v+1].ff+1, dp[2*v].ff + dp[2*v+1].ss+1));
        }
    }
}


/*
░░░░░░░░░
░░░░▄▀▀▀▀▀█▀▄▄▄▄░░░░
░░▄▀▒▓▒▓▓▒▓▒▒▓▒▓▀▄░░
▄▀▒▒▓▒▓▒▒▓▒▓▒▓▓▒▒▓█░
█▓▒▓▒▓▒▓▓▓░░░░░░▓▓█░
█▓▓▓▓▓▒▓▒░░░░░░░░▓█░
▓▓▓▓▓▒░░░░░░░░░░░░█░
▓▓▓▓░░░░▄▄▄▄░░░▄█▄▀░
░▀▄▓░░▒▀▓▓▒▒░░█▓▒▒░░
▀▄░░░░░░░░░░░░▀▄▒▒█░
░▀░▀░░░░░▒▒▀▄▄▒▀▒▒█░
░░▀░░░░░░▒▄▄▒▄▄▄▒▒█░
░░░▀▄▄▒▒░░░░▀▀▒▒▄▀░░
░░░░░▀█▄▒▒░░░░▒▄▀░░░
░░░░░░░░▀▀█▄▄▄▄▀ Kappa

*/



int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int g, c;
    cin >> n >> v;
    for(int i = 0; i <(n-1)/2; ++i){
        cin >> g >> c;
        a.eb(mp(g, c));
    }

    for(int i = (n+1)/2; i <(n+1); ++i){
        cin >> g;
        b[i] = g;
    }

    dfs(1);

    //for (int i = 1; i < n+1; ++i)
    //    cout << dp[i].ff << ' ' << dp[i].ss << ' '<< 'h' << '\n';

    if (v == 0)
        if (dp[1].ff != INF)
            cout << dp[1].ff;
        else
            cout << "IMPOSSIBLE";
    else
        if (dp[1].ss != INF)
            cout << dp[1].ss;
        else
            cout << "IMPOSSIBLE";
    return 0;
}
