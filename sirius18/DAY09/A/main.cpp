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

vector<int> p(MAXN, 0);
vector<int> rnk(MAXN, 1);


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

    int cnt = 0;
    for(auto i : e){
        if(!check(i.a, i.b)){
            cnt += i.c;
            unon(i.a, i.b);
        }
    }

    cout << cnt;
    return 0;
}
