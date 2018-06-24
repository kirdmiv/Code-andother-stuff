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
#define FI for(ll i = 0; i<n; ++i)
#define FI1 for(ll i = 1; i<n; ++i)
#define FJ for(ll j = 0; j<m; ++j)
#define FJ1 for(ll j = 1; j<m; ++j)

using namespace std;
using namespace __gnu_cxx;
using namespace __gnu_pbds;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef size_t sit;
typedef double db;
typedef unsigned int ui;
typedef tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;


struct Node{
    bool isLeaf = true;
    ll x = 0;
    Node() {}
    Node(ll val) : x(val), isLeaf(false) {}
    Node(ll val, bool leaf) : x(val), isLeaf(leaf) {}

    bool operator< (const Node& oth) const {
        return (x < oth.x);
    }
};


const ll INF = 1e9;
const ll MAXN = 100001;
ll n, x, k;
vector<Node> st(4 * MAXN, Node());
vector<ll> a;

void pull(ll v){
    //cerr << v;

    st[v].x = st[2*v+1].x + st[2*v].x;
}


void build(ll v, ll l, ll r){
    if (l == r - 1){
        //cerr << l;
        st[v] = Node(a[l], true);
        return;
    }
    ll m = (l + r) / 2;
    //cerr << v << ' ';
    build(2*v, l, m);
    //cerr << v << ' ';
    build(2*v+1, m, r);
    //cerr << v << ' ';
    pull(v);
}


ll getSum(ll v, ll l, ll r, ll tl, ll tr){
    //cerr << tl << ' ' << tr << '\n';
    if (r <= l || tr < l || tl > r)
        return 0;
    if (tl == l && tr == r)
        return st[v].x;
    //ll m = (l + r) / 2;
    ll tm = (tl + tr) / 2;
    ll v1 = getSum(2*v, l, min(tm, r), tl, tm);
    ll v2 = getSum(2*v+1, max(tm, l), r, tm, tr);
    return v1 + v2;
}


ll update(ll v, ll tl, ll tr, ll u, ll x){
    //cerr << v<< ' ';
    //if (tr <= tl)
    //    return;
    ll prev = 0;
    if (tl == tr - 1 && tl == u){
        prev = st[v].x;
        st[v].x = x;
        return prev;
    }
    st[v].x += x;
    ll tm = (tl + tr) / 2;
    if (u < tm)
        prev = update(2*v, tl, tm, u, x);
    else
        prev = update(2*v+1, tm, tr, u, x);
    st[v].x -= prev;
    return prev;
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ll l, r;
    char c;

    cin >> n;
    FI { cin >> x; a.eb(x);}
    cin >> k;
    //st.resize(4*(n+1));
    //cerr << st.size() << '\n';
    build(1, 0, n);
    //for (ll i = 0 ; i < 20; i++){
    //    cout << st[i].x << ' ' << st[i].ind << '\n';
    //}
    //return 0;
    //cerr << "sdfw";
    for (ll i=0; i<k;i++){
        cin >> c >> l >> r;
        if (c == 's')
            cout << getSum(1, l, r+1, 1, n+1) << ' ';
        else
            update(1, 0, n, l-1, r);
    }

    return 0;
}
