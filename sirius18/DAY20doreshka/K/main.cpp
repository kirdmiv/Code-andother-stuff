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

//file define
//#define INPUT_FILE "stdin.in"
//#define OUTPUT_FILE "stdout.out"

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

mt19937 random_ll;


void print(const vector<int> &v, char sep=' ', char end=' '){
    for (auto i : v){
        cout << i << sep;
    }
    cout << '\n';
}



const int INF = 1e9;
const int MAXN = 100;


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
░░░░░░░░▀▀█▄▄▄▄▀ KappaPRIDE(no tsveta ne vidno)

*/

struct Node;

struct Pointer {
	Node *ptr;
	Pointer();
	Pointer(int value);
	int value();
	ui priority();
	ui size();
	Pointer &left();
	Pointer &right();
	operator bool();
	void push();
	void pull();
};

struct Node {
	int val; ui pr, sz;
	Pointer l, r;
	Node(int value) : val(value), pr(random_ll()), sz(1) {}
	Node() : Node(0) {}
};

Pointer::Pointer() { ptr = nullptr; }
Pointer::Pointer(int value) { ptr = new Node(value); }
int Pointer::value() { return ptr->val; }
ui Pointer::priority() { return ptr->pr; }
ui Pointer::size() { return ptr? ptr->sz : 0; }
Pointer &Pointer::left() { return ptr->l; }
Pointer &Pointer::right() { return ptr->r; }
Pointer::operator bool() { return ptr != nullptr; }
void Pointer::push() {  }
void Pointer::pull() { assert(ptr); ptr->sz = left().size() + 1 + right().size(); }

ostream &operator<<(ostream &out, Pointer p) {
	vector<pair<Pointer, int>> q;
	q.pb(mp(p, 0));
	while (q.size()) {
		auto pr = q.back();
		int type = pr.second;
		Pointer v = pr.first;
		if (type) q.pop_back();
		else q.back().second = 1;
		if (v) {
			if (type == 0) {
				q.pb(mp(v.left(), 0));
			} else {
				out << v.value() << ' ';
				q.pb(mp(v.right(), 0));
			}
		}
	} return out;
}

Pointer operator+(Pointer l, Pointer r) {
	Pointer root, *u; int type;
	vector<Pointer *> us; vector<int> ts;
	us.pb(&root); ts.pb(0);
	while (ts.size()) {
		u = us.back(); type = ts.back();
		if (type == 0) {
			ts.back() = 1;
			if (l && r) {
				l.push(); r.push();
				if (l.priority() < r.priority())	*u = l, us.pb(&l.right()), l = l.right();
				else 								*u = r, us.pb(&r.left()), r = r.left();
				ts.pb(0);
			} else *u = (l? l : r);
		} else u->pull(), us.pop_back(), ts.pop_back();
	} return root;
}

void split(Pointer t, int k, Pointer &llink, Pointer &rlink) {
	Pointer *l = &llink, *r = &rlink; *l = *r = Pointer();
	while (t) {
		t.push();
		int l_size = t.left().size();
		if (k <= l_size) {
			*r = t;
			r = &(*r).left();
			t = t.left();
			*r = Pointer();
		} else {
			*l = t;
			l = &(*l).right();
			t = t.right();
			*l = Pointer();
			k -= l_size + 1;
		}
	} *l = *r = Pointer();
}




/*
░░▄▄▄▄▄▓▓▓▄▄▄░░░░░
░░░░▄▄▓▀▀▀▀▀▀▓▓▓▓▓▓▄░░░
░░▄▄▓▀▀░░░░░░░▒▒▒▒▒▀▓▄░
░▐▓▓▌░░░░░░░░░░░░▒▒▒▒▓▌
░▐▓▒░░▄▒▒▓▄▄▒▒▒░▒▄▄▄▒▒▓
░▓▓▌░░░░░▒▒▒▒▀▒▒▓▓▓▓▓▓▓
░▐▓░░░░▒▒▓(◐)▓░░░▒▓▓(◐)▒▓
█░▀▄░█▄█▀▄▄░▀░▀▄▄▀░░█░█
░█░░░▀▄█▄█░█▀▄▄▄▄▄▀██░█
░░█░░░░█░███▄█▄█▄███░░█
░░░█░░░▀▀█░█▀█▀█▀███░█
░░░░▀▄░░░░▀▀▄█▄█▄█▄▀░█
░░░░░░▀▄▄░▒▒▒░░░░░░░░░█
░░░░░░░░░▀▀▄▄▄▄▄▄▄▄▄▄▀
*/


/*
Спасибо, мистер Дудец!
░░░░░░▄▄▄░░▄██▄░░░
░░░░░▐▀█▀▌░░░░▀█▄░░░
░░░░░▐█▄█▌░░░░░░▀█▄░░
░░░░░░▀▄▀░░░▄▄▄▄▄▀▀░░
░░░░▄▄▄██▀▀▀▀░░░░░░░
░░░█▀▄▄▄█░▀▀░░
░░░▌░▄▄▄▐▌▀▀▀░░
▄░▐░░░▄▄░█░▀▀ ░░
▀█▌░░░▄░▀█▀░▀ ░░
░░░░░░░▄▄▐▌▄▄░░░
░░░░░░░▀███▀█░▄░░
░░░░░░▐▌▀▄▀▄▀▐▄░░
░░░░░░▐▀░░░░░░▐▌░░
░░░░░░█░░░░░░░░█░░░
*/

template<class A> void addlog(A a) { cout << a << endl; }
template<class A, class... B> void addlog(A a, B... b)
{ cout << a << ' '; addlog(b...); }



int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    #ifdef INPUT_FILE
    freopen(INPUT_FILE, "r", stdin);
    #endif // INPUT_FILE

    #ifdef OUTPUT_FILE
    freopen(OUTPUT_FILE, "w", stdout);
    #endif // OUTPUT_FILE

    Pointer a, l, r, sr, sl;

    int n, m;
    cin >> n >> m;
    FI{
        a = a + Pointer(i+1);
    }
    //addlog(a);

    int le, ri;
    FJ{
        cin >> le >> ri;
        le--;
        ri--;
        if (le == 0 && ri == 0)
            continue;
        //if (ri - le + 2 > n/2)
        //    ri--;
        split(a, le, l, r);
        split(r, ri-le+1, sl, sr);
        a = sl + l + sr;
        //addlog(a);
    }

    addlog(a);
    return 0;
}
