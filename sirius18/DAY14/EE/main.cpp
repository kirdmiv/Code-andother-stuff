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
typedef size_t s_t;
typedef double db;
typedef unsigned int ui;
typedef tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

const ll INF = 1e9;
const ll MAXN = 10001;



struct Node{
    ll x = 0, add = 0;
    s_t sz = 1;
    bool leaf = false;
    Node() {}
    Node(ll val, ll a, bool lf, s_t siz) : x(val),  add(a), leaf(lf), sz(siz) {}
    Node(ll val, ll a) : x(val),  add(a) {}
    Node(ll val, ll a, s_t siz) : x(val),  add(a), sz(siz) {}
    Node(ll val) : x(val) {}
};


ll n, x, k;
vector<Node> st(4 * MAXN, Node());
vector<ll> a;


void pull(ll v){
    //if (!st[v].leaf){
        st[v].x = st[2*v].x + st[2*v+1].x;
        st[v].sz = st[2*v].sz + st[2*v+1].sz;
    //    cerr << v <<' ';
    //}
}


void push(ll v){
    if (!st[v].leaf){
        st[2*v].add += st[v].add;
        st[2*v].add += st[v].add;
    }
    st[v].x += st[v].add * st[v].sz;
    st[v].add = 0;
}


void build(ll v, ll l, ll r){
    if (l == r-1){
        st[v] = Node(0, 0, true, 1);
        return;
    }

    ll m =(l+ r) / 2;
    build(2*v, l, m);
    build(2*v+1, m, r);
    pull(v);
}


void update(ll v, ll l, ll r, ll tl, ll tr, ll x){
    //cerr << v << ' ';
    if (r <= l || tr < l || tl > r)
        return;
    if (tl == l && tr == r){
        st[v].add += x;
        push(v);
        return;
    }
    //ll m = (l + r) / 2;
    push(v);
    ll tm = (tl + tr) / 2;
    update(2*v, l, min(tm, r), tl, tm, x);
    update(2*v+1, max(tm, l), r, tm, tr, x);
    pull(v);
}


ll getSum(ll v, ll l, ll r, ll tl, ll tr){
    //cerr << tl << ' ' << tr << '\n';
    if (r <= l || tr < l || tl > r)
        return 0;
    if (tl == l && tr == r)
        return st[v].x;
    //ll m = (l + r) / 2;
    push(v);
    ll tm = (tl + tr) / 2;
    ll v1 = getSum(2*v, l, min(tm, r), tl, tm);
    ll v2 = getSum(2*v+1, max(tm, l), r, tm, tr);
    pull(v);
    return v1 + v2;
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ll l, r;
    char mode;

    cin >> n >> k;
    build(1, 0, n);

    //for (int i = 0 ; i < 20; i++){
    //    cout << st[i].x << ' ' << st[i].sz << '\n';
    //}
    //return 0;

    for(ll i = 0; i < k; i++){
        cin >> mode >> l >> r;
        if(mode == '1'){
            cin >> x;
            //st[1].add += x;
            update(1, l, r, 0, n, x);
        } else{
            cout << getSum(1, l, r, 0, n) << '\n';
        }
    }

    return 0;
}
