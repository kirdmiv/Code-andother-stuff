#include <bits/stdc++.h>
#include "ext/rope"
#include "ext/pb_ds/detail/standard_policies.hpp"
#include "ext/pb_ds/assoc_container.hpp"

#define np nullptr
#define mp make_pair
#define pb push_back
#define eb emplace_back
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

int n;

struct Node{
    ll prior, value;
    st sz;
    Node* left;
    Node* right;

    Node(ll p, ll v) : prior(p), value(v), sz(0), left(np), right(np) {};
};


void pull(Node* tree){
    int lsz=0, rsz=0;
    if(tree->left == np){
        lsz = 0;
    } else{
        lsz = tree->left->sz;
    }
    if(tree->right == np){
        rsz = 0;
    } else{
        rsz = tree->right->sz;
    }
    tree->sz = lsz + rsz + 1;
}


Node* Merge(Node* left, Node* right){
    if(left == np)
        return right;
    if(right == np)
        return left;
    if (left->prior < right->prior){
        left->right = Merge(left->right, right);
        pull(left);
        return left;
    }
    right->left = Merge(left, right->left);
    pull(right);
    return right;
}


pair<Node*, Node*> split(Node* tree, ll x){
    if(tree == np)
        return mp(np, np);
    st ind;
    if (tree->left == np)
        ind = 0;
    else
        ind = tree->left->sz;
    pair<Node*, Node*> nodes;
    if (x <= ind){
        nodes = split(tree->left, x);
        Node* left = nodes.ff;
        tree->left = nodes.ss;
        pull(tree);
        //cerr << x << '\n';
        return mp(left, tree);
    }
    else{
        nodes = split(tree->right, x-ind-1);
        tree->right = nodes.ff;
        Node* right = nodes.ss;
        pull(tree);
        //cerr << x << '\n';
        return mp(tree, right);
    }
}


ll get(Node* tree, ll k){
    pair<Node*, Node*> nodes = split(tree, k);
    ll ans = nodes.ss->value;
    Merge(nodes.ff, nodes.ss);
    return ans;
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    mt19937_64 gen;
    seed_seq sseq{1, 2};
    gen.seed(sseq);

    char op;
    int k;

    cin >> n;
    cin >> op >> k;

    Node* root = np;
    pair<Node*, Node*> nodes;

    ll prev = 0;

    FI{
        //cerr << i << ' ';
        cin >> op >> k;
        Node* new_Node = new Node(gen(), k);
        if(op == '+'){
            k = (k + prev) % INF;
            nodes = split(tree, k);
            root = Merge(nodes.ff, new_Node);
            root = Merge(root, nodes.ss);
            prev = 0;
            //cerr << root->left;
        }
        else{
            //cerr << "SAFAFSUAKDA";
            pair<Node*, Node*> nodes = split(root, k);
            ll ans;
            if (nodes.ss == np)
                ans = -1;
            else
                ans = nodes.ss->value;
            //cerr << "SAFAFSUAKDA";
            root = Merge(nodes.ff, nodes.ss);
            cout << ans << '\n';
            prev = ans;
        }
    }

    return 0;
}
