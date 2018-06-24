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
const int MAXN = 101;

vector<int> g[MAXN];
vector<int> p(MAXN, 0);
vector<int> rnk(MAXN, 1);
vector<int> used(MAXN, 0);


int get(int v){
    if (p[v] == v)
        return v;
    return p[v] = get(p[v]);
}

bool check(int v, int u){
    return get(v) == get(u);
}

void unon(int v, int u){
    v = get(v);
    u = get(u);
    if (rnk[v] > rnk[u]){
        p[u] = v;
        return;
    }
    if (rnk[v] == rnk[u])
        rnk[u]++;
    p[v] = u;
}

struct Edge{
    int a, b, c;

    Edge(int beg, int en, int cost) : a(beg), b(en), c(cost) {}

    bool operator< (const Edge& oth) const{
        return c < oth.c;
    }
};

void dfs(int v){
    used[v] = 1;
    for (auto i : g[v]){
        if (!used[i])
            dfs(i);
    }
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m, a, b, c;
    cin >> n >> m;

    vector<Edge> e;
    FJ{
        cin >> a >> b >> c;
        b--; a--;
        e.eb(Edge(a, b, c));
    }

    FI p[i] = i;
    stable_sort(e.begin(), e.end());

    vector<Edge> mste;
    vector<ll> ans;
    ll cnt = 0;
    for (int k=0; k<m; k++){
        int t = 0;
        cnt = 0;
        rnk.assign(MAXN, 1);
        FI p[i] = i;
        for(auto i : e){
            if(!check(i.a, i.b) && t != k){
                cnt += i.c;
                unon(i.a, i.b);
                //used[i.a] = 1;
                //used[i.b] = 1;
                g[i.a].eb(i.b);
                g[i.b].eb(i.a);
            }
            t++;
        }
        int co = 0;
        FI{
            if(!used[i]){
                dfs(i);
                co++;
            }
        }

        cout << co << '\n' << '\n';
        FI{
            for(j : g[i])
                cout << j << ' ';
            cout << '\n';
        }
        cout << cnt << '\n' << '\n';

        if (co <= 1)
            ans.pb(cnt);
        used.assign(MAXN, 0);
        FI{
        g[i].clear();
        }
    }
    stable_sort(ans.begin(), ans.end());
    ll asn1 = ans[0];
    cout << asn1 << ' ';
    for(auto i : ans){
        if (i != asn1){
            cout << i;
            break;
        }
    }
    return 0;
}
