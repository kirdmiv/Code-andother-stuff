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
typedef size_t st;
typedef double db;
typedef unsigned int ui;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

const int INF = 1e9;
const int MAXN = 50002;


const ull p1 = 2000000089, p2 = 2000000137;
const ull b = 127;
const ull sq1 = p1 * p1;
const ull sq2 = p2 * p2;

string s, t;
ull h1[2][MAXN], h2[2][MAXN], bpow[2][MAXN];


int fast_eq(int i){
    int d = t.size();
    //cout << ((sq + h1[0][i+d] - (h1[0][i] * bpow[0][d]) % p1) %p1) << '\n';
    //cout << (h1[0][i+d] - (h1[0][i] * bpow[0][d]) % p1)<< ' ' << h2[0][d] << '\n';
    //cout << ((h1[0][i+d] - (h1[0][i] * bpow[0][d]) - (h2[0][d] * bpow[0][d])) %p1) << '\n';
    return ((sq1 + h1[0][i+d] - (h1[0][i] * bpow[0][d])) % p1 - h2[0][d]) == 0 &&
            ((sq2 + h1[1][i+d] - (h1[1][i] * bpow[1][d])) % p2 - h2[1][d]) == 0;
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    cin >> s;


    h1[0][0] = 0;
    h1[1][0] = 0;
    bpow[0][0] = 1;
    bpow[1][0] = 1;

    for(int i = 1; i<s.size()+1; ++i){
            h1[0][i] = (h1[0][i-1] * b + s[i-1]) % p1;
            h1[1][i] = (h1[1][i-1] * b + s[i-1]) % p2;
            bpow[0][i] = (bpow[0][i-1] * b) % p1;
            bpow[1][i] = (bpow[1][i-1] * b) % p2;
            //cout << h1[0][i] << '\n';
    }

    reverse(s.begin(), s.end());
    h2[0][0] = 0;
    h2[1][0] = 0;

    for(int i = 1; i<t.size()+1; ++i){
            h2[0][i] = (h2[0][i-1] * b + s[i-1]) % p1;
            h2[1][i] = (h2[1][i-1] * b + s[i-1]) % p2;
            //cout << h2[0][i] << '\n';
    }

    for(int i = 0; i<s.size() - t.size() + 1; ++i){
        if(fast_eq(i))
            cout << i << ' ';
    }

    return 0;
}
