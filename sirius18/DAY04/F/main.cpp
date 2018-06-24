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
typedef int ui;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;


struct longNumbers
{
    ui base;
    char sign;
    vector<ui> a;
    longNumbers(ui b, char s, vector<ui> &v) : base(b), sign(s), a(v){}
    longNumbers(){}

    bool operator < (const longNumbers& oth) const
    {
        if (a.size() < oth.a.size()) return 1;
        if (a.size() > oth.a.size()) return 0;
        return a < oth.a;
    }

    bool operator <= (const longNumbers& oth) const
    {
        return a < oth.a || a == oth.a;
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





/*
    longNumbers operator - (const longNumbers& x) const
    {
        vector<ui> c;
        int mx = max(a.size(), x.a.size());
        c.assign(mx, 0);
        int mn = min(a.size(), x.a.size());

        for(int i = 0; i < a.size(); ++i){
            c[i] += a[i];
            if(i < x.a.size() && a[i] >= x.a[i])
                c[i] -= x.a[i];
            else if(i < x.a.size()){
                int j = i+1;
                while(!a[j])
                    ++j;
                c[j] -= 1;
                c[i] += base;
                c[i] -= x.a[i];
            }
        }
        while(c.back() == 0 && c.size() > 1) c.pop_back();
        return longNumbers(base, sign, c);
    }
};
*/

    longNumbers operator+ (const longNumbers& oth) const
    {
        vector<ui> c;
        int mx = max(a.size(), oth.a.size());
        c.assign(mx+1, 0);
        int mn = min(a.size(), oth.a.size());

        for(int i = 0; i < mx; ++i){
            c[i] = c[i];
            if (i < a.size())
                c[i] += a[i];
            if (i < oth.a.size())
                c[i] += oth.a[i];
            c[i+1] = c[i] / base;
            c[i] %= base;
        }
        if (c.back() == 0) c.pop_back();
        return longNumbers(base, sign, c);
    }

    longNumbers operator* (const longNumbers& oth) const
    {
        vector<ui> c;
        c.assign(a.size()+oth.a.size(), 0);

        for(int i = 0; i < a.size(); ++i)
            for(int j = 0; j < oth.a.size(); ++j)
                c[i+j] += a[i] * oth.a[j];
        for(int i = 0; i < a.size()+oth.a.size()-1; ++i){
            c[i+1] += c[i] / base;
            c[i] %= base;
        }
        while(c.back() == 0 && c.size() > 1) c.pop_back();
        return longNumbers(base, sign, c);
    }

    longNumbers operator-(const longNumbers &num) const {
        longNumbers c;
        c.a.resize(a.size());
        for (int i = 0; i < a.size(); i++) {
            c.a[i] += a[i];
            if (i < num.a.size()) c.a[i] -= num.a[i];
            if (c.a[i] < 0) {
                --c.a[i + 1];
                c.a[i] = base + c.a[i];
            }
        }
        while (c.a.back() == 0 && c.a.size() > 1) c.a.pop_back();
        return c;
    }

    longNumbers operator / (const ll& x) const
    {
        string ans = "";
        //vector<ui> c;
        //c.assign(a.size()+oth.a.size(), 0);
        int p = 0;
        //cout << ans << ' ' << p << '\n';
        for(int i = a.size()-1; i > -1; --i){
            p = p * base + a[i];
            ans += to_string(p / x);
            p %= x;
            //cout << ans << ' ' << p << '\n';
        }
        ui uix;
        string xs;
        vector<ui> vx;
        for(int i = ans.size()-1; i > -1; i-=2){
            xs = ans[i];
            if (i - 1 > -1)
                xs = ans[i-1] + xs;
            //cout << as << ' ' << x << ' ' <<as[i]<< as[i-1] << '\n';
            uix = (ui)stoi(xs);
            vx.eb(uix);
        }
        longNumbers c = longNumbers(100, 0, vx);
        return c;
    }

    longNumbers operator/ (const longNumbers& oth){
        vector<int> lol(1, 1);
        vector<int> one(1, 1);
        vector<int> zr(1, 0);
        longNumbers onel = longNumbers(100, 0, one);
        longNumbers zrl = longNumbers(100, 0, zr);
        longNumbers l = longNumbers(100, 0, lol);
        longNumbers r = *this, m;
        //r = r + onel;
        //vector<int> one(1, 1);
        vector<int> a1 = (*(this)).a;
        reverse(a1.begin(), a1.end());
        longNumbers a3 = longNumbers(100, 0, a1);
        while (r - l > onel){
            m = (r + l) / 2LL;
            vector<int> a2 = (m * oth).a;
            reverse(a2.begin(), a2.end());
            longNumbers a4 = longNumbers(100, 0, a2);
            if(a3 < a4)
                r = m;
            else
                l = m;
        }
        while (l.a.back() == 0 && l.a.size() > 1) l.a.pop_back();
        while (r.a.back() == 0 && r.a.size() > 1) r.a.pop_back();
        vector<int> a2 = (r * oth).a;
        reverse(a2.begin(), a2.end());
        longNumbers a4 = longNumbers(100, 0, a2);
        if (a3 < a4 && a4 > onel){
            r = r - onel;
            vector<int> a2 = (r * oth).a;
            reverse(a2.begin(), a2.end());
            longNumbers a4 = longNumbers(100, 0, a2);
            //for(int i=0;i<r.a.size();++i)
            //    cout << r.a[i] << ' ';
            //cout<<'\n';
            }

        return r;
    }

};

int main()
{
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);
    freopen("stress.in", "r", stdin);
    freopen("stress.out", "w", stdout);
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
    //reverse(va.begin(), va.end());
    //reverse(vb.begin(), vb.end());
    longNumbers a = longNumbers(100, 0, va);
    longNumbers b = longNumbers(100, 0, vb);

    longNumbers c = longNumbers(100, 0, vb);
    c = a/b;
    vector<ui> vc = c.a;
    reverse(vc.begin(), vc.end());
    cout << vc[0];
    for(int i = 1; i<vc.size(); ++i){
        cout << setw(2) << setfill('0') << vc[i];
    }
    //vector<ui> vc = c.a;
    //reverse(vc.begin(), vc.end());
    //cout << vc[0];
    //for(int i = 1; i<vc.size(); ++i){
    //    cout << setw(2) << setfill('0') << vc[i];
    //}
    //for(int i = 0; i < va.size(); ++i){
    //    cout << va[i] << ' ';
    //}

    return 0;
}
