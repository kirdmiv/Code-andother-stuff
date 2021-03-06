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
typedef size_t sit;
typedef double db;
typedef unsigned int ui;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;


struct Node{
    bool isLeaf = true;
    int x = 0, ind = 0;
    Node() {}
    Node(int val, int i) : x(val), ind(i), isLeaf(false) {}
    Node(int val, int i, bool leaf) : x(val), ind(i), isLeaf(leaf) {}

    bool operator< (const Node& oth) const {
        return (x < oth.x) || (x == oth.x && ind > oth.x);
    }
};


const int INF = 1e9;
const int MAXN = 100001;
int n, x, k;
vector<Node> st(4 * MAXN, Node());
vector<int> a;

void pull(int v){
    //cerr << v;

    st[v].x = __gcd(st[2*v+1].x, st[2*v].x);

}


void build(int v, int l, int r){
    if (l == r - 1){
        //cerr << l;
        st[v] = Node(a[l], l, true);
        return;
    }
    int m = (l + r) / 2;
    //cerr << v << ' ';
    build(2*v, l, m);
    //cerr << v << ' ';
    build(2*v+1, m, r);
    //cerr << v << ' ';
    pull(v);
}


pair<int, int> getMax(int v, int l, int r, int tl, int tr){
    //cerr << tl << ' ' << tr << '\n';
    if (r <= l || tr < l || tl > r)
        return mp(0, -1);
    if (tl == l && tr == r)
        return mp(st[v].x, st[v].ind);
    int m = (l + r) / 2;
    int tm = (tl + tr) / 2;
    pair<int, int> v1 = getMax(2*v, l, min(tm, r), tl, tm);
    pair<int, int> v2 = getMax(2*v+1, max(tm, l), r, tm, tr);
    return mp(__gcd(v1.ff, v2.ff), -1);
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int l, r;

    cin >> n;
    FI { cin >> x; a.eb(x);}
    cin >> k;
    //st.resize(4*(n+1));
    //cerr << st.size() << '\n';
    build(1, 0, n);
    //for (int i = 0 ; i < 20; i++){
    //    cout << st[i].x << ' ' << st[i].ind << '\n';
    //}
    //return 0;
    //cerr << "sdfw";
    for (int i=0; i<k;i++){
        cin >> l >> r;

        cout << getMax(1, l, r+1, 1, n+1).ff << ' ';
    }

    return 0;
}
