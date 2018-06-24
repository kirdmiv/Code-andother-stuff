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
const int MAXN = 500;
vector<int> a[MAXN];
vector<int> used(MAXN, false);
vector<int> pr(MAXN, -1);
vector<int> ansv;
int ans = 0, lt = 0;
int n, m, x;

void dfs(int v, int pre){
    used[v] = 1;
    pr[v] = pre;
    FI{
        if (ans)
            return;
        if(a[v][i] && !used[i]){
            dfs(i, v);
        }
        else if (a[v][i] && used[i]==1 && i != pre){
            //cout << v << '\n';
            ans = 1;
            lt = v;
            int slt = pr[i];
        bool f = true;
        while(lt != -1 && (lt != slt || f)){
            ansv.pb(lt);
            //cout << lt <<' ' << slt << '\n';
            lt = pr[lt];
            f = false;
        }
        cout << "YES\n" << ansv.size() << '\n';
        for(auto i : ansv)
            cout << i+1 << ' ';
        exit(0);
    }
            //return;
        }
        used[v] = 2;
    }
    //used[v] = 2;



int main()
{
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);

    cin >> n;
    m = n;
    FI{
        FJ{
            cin >> x;
            a[i].pb(x);
        }
    }
    //cout << "ok\n";
    FI{
        //cout << i << ' ' << used[i] << '\n';
        if (!used[i])
            dfs(i, -1);
    }
    cout << "NO";
    return 0;
    //cout << "ok\n";
    if(!ans)
        cout << "NO";
    else{
        int slt = lt;
        bool f = true;
        while(lt != -1 && (lt != slt || f)){
            ansv.pb(lt);
            //cout << lt <<' ' << slt << '\n';
            lt = pr[lt];
            f = false;
        }
        cout << "YES\n" << ansv.size() << '\n';
        for(auto i : ansv)
            cout << i+1 << ' ';
    }
    return 0;
}
