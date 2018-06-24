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
const int MAXN = 10000;
const int KOLICHESTVO = 10000;

int n, x, k;
string s, sts;
vector<int> g[MAXN];
vector<int> p(MAXN, -1);
vector<int> used(MAXN, -1);
vector<int> inside(KOLICHESTVO, 0);


int dfs(int v){
    used[v] = k;
    //cout << v << ' ';
    //if (v == 0){
        //cout << g[0][6];
    //}
    for(auto i : g[v]){
        //cout << i << ' ';
        if(p[i] == -1){
            p[i] = v;
            return 1;
        }
    }
    for(auto i : g[v]){
        //cerr << p[i] << ' ';
        try{
        if(!(used[i]==k) && dfs(p[i])){
            p[i] = v;
            return 1;
        }}
        except{
            continue;
        }
    }
    return 0;
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    cin >> sts;



    set<int> st;
    FI{

        cin >> s;
        for(int j=0; j<s.size(); ++j){
            int p = s[j] - 'A';
            if(st.count(p) == 0){
                for(int l=0; l<sts.size(); l++)
                    if(sts[l] == s[j])
                        g[i].pb(l);
                st.insert(p);
                //cout << i << ' ' << p << '\n';
            }
        }
        st.clear();
    }
    //FI{
    //for(j : g[i])
    //    cout << j << ' ';
    //cout << '\n';
    //return 0;
    //}


     //if (n < sts.size()){
     //   cout << "NO\n";
     //   return 0;
    //s}


    int ans = 0;
    for(k=0; k<n; k++){
        ans += dfs(k);
        //cout << k << ' ' << ans << '\n';
    }

    //cout << ans;
    //for(int i=0; i<MAXN; i++){
    //    if(inside[i] && p[i] == -1){
    //        cout << "NO\n";
    //        return 0;
    //    }
    //}

    if (ans < sts.size()){
        cout << "NO\n";
        return 0;
    }
    cout << "YES\n";
    for(int i=0; i<sts.size(); i++){
        cout << p[i]+1 << ' ';
        //    return 0;
        }
    //}
    return 0;
}



/*
5
ZAZA
ADFZ
AFZAS
AZAGFS
JHFS
AADSF
*/
