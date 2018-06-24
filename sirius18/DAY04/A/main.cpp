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


struct longNumbers
{
    ui base;
    char sign;
    vector<ui> a;
    longNumbers(ui b, char s, vector<ui> &v) : base(b), sign(s), a(v){}

    bool operator < (const longNumbers& oth) const
    {
        if (a.size() < oth.a.size()) return 1;
        if (a.size() > oth.a.size()) return 0;
        return a < oth.a;
    }

    bool operator > (const longNumbers& oth) const
    {
        if (a.size() > oth.a.size()) return 1;
        if (a.size() < oth.a.size()) return 0;
        return a > oth.a;
    }

    bool operator == (const longNumbers& oth) const
    {
        if (a.size() < oth.a.size()) return 0;
        if (a.size() > oth.a.size()) return 0;
        return a == oth.a;
    }

};

int main()
{
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);
    string as, bs, x;
    ui uix;
    cin >> as >> bs;

    //cout << as << '\n';
    vector<ui> va, vb;
    for(int i = as.size()-1; i > -1; i-=2){
        x = as[i];
        if (i - 1 > -1)
            x = as[i-1] + x;
        //cout << as << ' ' << x << ' ' <<as[i]<< as[i-1] << '\n';
        uix = (ui)stoi(x);
        va.eb(uix);
    }
    for(int i = bs.size()-1; i > -1; i-=2){
        x = bs[i];
        if (i - 1 > -1)
            x = bs[i-1] + x;
        //cout << as << ' ' << x << ' ' <<as[i]<< as[i-1] << '\n';
        uix = (ui)stoi(x);
        vb.eb(uix);
    }
    reverse(va.begin(), va.end());
    reverse(vb.begin(), vb.end());
    longNumbers a = longNumbers(100, 0, va);
    longNumbers b = longNumbers(100, 0, vb);
    if(a > b)
        cout << '>';
    else if (a < b)
        cout << '<';
    else
        cout << '=';
    //for(int i = 0; i < va.size(); ++i){
    //    cout << va[i] << ' ';
    //}

    return 0;
}
