#include <bits/stdc++.h>
#include "ext/rope"
#include "ext/pb_ds/detail/standard_policies.hpp"
#include "ext/pb_ds/assoc_container.hpp"

#define mp make_pair
#define pb push_back
#define eb emplace_back
#define sf scanf
#define ff first
#define ss second
#define FI for(int i = 0; i<n; ++i)
#define FI1 for(int i = 1; i<n; ++i)


using namespace std;
using namespace __gnu_cxx;
using namespace __gnu_pbds;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef size_t st;
typedef double db;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

struct Chel
{
    string sn; string n; string c; string d;
    Chel(string sni, string ni, string ci, string di) : sn(sni), n(ni), c(ci), d(di) {}

    bool operator <(const Chel& a) const
    {
        int clf, cls;
        string cf, cs;
        if (c.size() == 2){
            clf = c[0] - '0';
            cf = c[1];
        }
        else{
            clf = 10 + (c[1] - '0');
            cf = c[2];
        }
        if (a.c.size() == 2){
            cls = a.c[0] - '0';
            cs = a.c[1];
        }
        else{
            cls = 10 + (a.c[1] - '0');
            cs = a.c[2];
        }
        return (clf < cls) || ((clf == cls) & cf < cs) || (((clf == cls) & cf == cs) & sn < a.sn);
    }
};

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    vector<Chel> v;
    string sn, nm, c, d;
    cin >> n;
    FI{
        cin >> sn >> nm >> c >> d;
        v.eb(Chel(sn, nm, c, d));
    }
    sort(v.begin(), v.end());
    FI{
        cout << v[i].c << ' ' << v[i].sn << ' ' << v[i].n << ' ' << v[i].d << '\n';
    }
    return 0;
}
