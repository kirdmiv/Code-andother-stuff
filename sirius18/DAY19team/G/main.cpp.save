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


void print(const vector<int> &v, char sep=' ', char end=' '){
    for (auto i : v){
        cout << i << sep;
    }
    cout << '\n';
}



const int INF = 1e9;
const int MAXN = 100;
const int base_size = 5;
const int base = 100000;


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


struct Number {
    vector<ll> num;
    bool sign = 0;

    Number(const string &s) {
        vector<ll> tmp;
        string cur;
        int first_block = s.size() % base_size;
        int pos = 0;
        if (first_block) {
            for (; pos < first_block; pos++) {
                cur += s[pos];
            }
            tmp.push_back(stoll(cur));
            cur = "";
        }
        for (int i = pos; i < s.size(); i++) {
            cur += s[i];
            if (cur.size() == base_size) {
                tmp.push_back(stoul(cur));
                cur = "";
            }
        }
        reverse(tmp.begin(), tmp.end());
        num = tmp;
    }

    Number(ll x) : Number(to_string(x)) {}

    Number() {}

    int compareTo(const Number &oth) const {
        if (oth.num.size() > num.size()) return -1;
        if (oth.num.size() < num.size()) return 1;
        for (int i = num.size() - 1; i >= 0; i--) {
            if (num[i] < oth.num[i]) return -1;
            if (num[i] > oth.num[i]) return 1;
        }
        return 0;
    }

    bool operator<(const Number &oth) const {
        return compareTo(oth) == -1;
    }

    bool operator>(const Number &oth) const {
        return compareTo(oth) == 1;
    }

    bool operator==(const Number &oth) const {
        return compareTo(oth) == 0;
    }

    bool operator!=(const Number &oth) const {
        return !(*(this) == oth);
    }

    friend istream &operator>>(istream &is, Number &num) {
        string tmp;
        is >> tmp;
        Number tmp1(tmp);
        num = tmp1;
        return is;
    }

    friend ostream &operator<<(ostream &os, const Number &Num) {
        if (Num.sign) {
            cout << '-';
        }
        for (int i = Num.num.size() - 1; i >= 0; i--) {
            if (i != Num.num.size() - 1) os << setw(base_size) << setfill('0') << abs(Num.num[i]);
            else os << Num.num[i];
        }
        return os;
    }

    Number operator+(const Number &oth) const {
        Number c;
        c.num.resize(max(num.size(), oth.num.size()) + 1);
        for (int i = 0; i < max(num.size(), oth.num.size()); i++) {
            if (i < num.size()) c.num[i] += num[i];
            if (i < oth.num.size()) c.num[i] += oth.num[i];
            c.num[i + 1] = c.num[i] / base;
            c.num[i] %= base;
        }
        if (c.num.back() == 0) c.num.pop_back();
        return c;
    }

    Number operator-(const Number &num) const {
        Number c;
        Number oth = min(num, *(this));
        Number that = max(num, *(this));
        if (that == num && that != oth) c.sign = 1;
        c.num.resize(max(that.num.size(), oth.num.size()));
        for (int i = 0; i < max(that.num.size(), oth.num.size()); i++) {
            c.num[i] += that.num[i];
            if (i < oth.num.size()) c.num[i] -= oth.num[i];
            if (c.num[i] < 0) {
                --c.num[i + 1];
                c.num[i] = base + c.num[i];
            }
        }
        while (c.num.back() == 0 && c.num.size() > 1) c.num.pop_back();

        return c;
    }

    Number operator*(const Number &oth) const {
        Number result;
        result.num.resize(num.size() + oth.num.size());
        for (int i = 0; i < num.size(); i++) {
            for (int j = 0; j < oth.num.size(); j++) {
                result.num[i + j] += num[i] * oth.num[j];
            }
        }
        for (int i = 0; i < num.size() + oth.num.size() - 1; i++) {
            result.num[i + 1] += result.num[i] / base;
            result.num[i] %= base;
        }
        while (result.num.back() == 0 && result.num.size() > 1) result.num.pop_back();
        return result;
    }

    Number operator*(const ll &oth) const {
        ll carry = 0;
        Number c;
        c.num.resize(num.size());
        for (int i = 0; i < num.size(); i++) {
            c.num[i] = num[i] * oth;
            c.num[i] += carry;
            carry = c.num[i] / base;
            c.num[i] %= base;
        }
        while (carry > 0) c.num.push_back(carry % base), carry /= base;
        return c;
    }

    Number operator/(const ll &oth) const {
        ll mod = 0;
        Number result;
        result.num.resize(num.size());
        for (int i = num.size() - 1; i >= 0; --i) {
            ll cur = mod * base + num[i];
            result.num[i] = (cur / oth);
            mod = cur % oth;
        }
        while (result.num.back() == 0 && result.num.size() > 1) result.num.pop_back();
        return result;
    }

    ll operator%(const ll &oth) const {
        ll mod = 0;
        Number result;
        result.num.resize(num.size());
        for (int i = num.size() - 1; i >= 0; --i) {
            ll cur = mod * base + num[i];
            result.num[i] = (cur / oth);
            mod = cur % oth;
        }
        return mod;
    }


    Number operator/(const Number &num) const {
        Number l("0"), r = *(this) + 1;
        while (r - l > 1) {
            Number m = (l + r) / 2;
            if (m * num > *(this)) {
                r = m;
            } else {
                l = m;
            }
        }
        return l;
    }

    Number operator%(const Number &num) const {
        return *(this) - num * (*(this) / num);
    }
};


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

ll A, B, C, D, E, F;

ll mx, mi;

vector<pair<ll, ll>> divi(long long n) {
    ll i = mi;
    vector<pair<ll, ll>> ans;
    ll sq = sqrt(n + 0.5);
    while (i <= sq) {
        if (n % i == 0) {
            ans.eb(mp(i, n / i));
        }
        i++;
    }
    return ans;
}

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

    cin >> A >> B >> C >> D >> E >> F;
    Number a = Number(to_string(A)), b = Number(to_string(B)), c = Number(to_string(C)), d = Number(to_string(D)),
    e = Number(to_string(E)), f = Number(to_string(F));
    //Number costil = Number("1000000000000");
    if (e > b * d || f < a * c) {
        cout << "NO";
        return 0;
    } else {
        mx = max(B, D);
        mi = min(A, C);
        if (a * c > e){
            E = A * C;
        }
        if (b * d < f){
            F = B * D;
        }
        bool fl = false;
        int counter = 0;
        for (ll i = F; i >= E && !fl; --i) {
            if (counter > 1000) break;
            auto divs = divi(i);
            for (auto d : divs) {
                if (d.first <= B && d.first >= A && d.second <= D && d.second >= C) {
                    fl = true;
                    cout << "YES" << endl;
                    cout << d.first << " " << d.second;
                    return 0;
                }
                if (d.first <= D && d.first >= C && d.second <= B && d.second >= A) {
                    fl = true;
                    cout << "YES" << endl;
                    cout << d.second << " " << d.first;
                    return 0;
                }
                counter++;
            }
        }
        if (!fl) cout << "NO" << endl;
    }
    return 0;
}
