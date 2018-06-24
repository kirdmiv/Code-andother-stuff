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

const int INF = 1e9;
const int MAXN = 100;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m, p;
    cin >> n >> m >> p;

    int c = ceil((double)(n + m) / 2);
    if (n / 2 >= p){
        cout << "P " << p*2-1 << '\n';
        cout << "P " << p*2 << '\n';
    }

    if (n / 2 + 1 == p && n%2==1 && m%2==1){
        cout << "P " << n << '\n';
        cout << "C " << m-1 << '\n';
    } else if (n / 2 + 1 == p && n%2==1)
    {
        cout << "P " << n << '\n';
        cout << "- -" << '\n';
    }
    if (n / 2 + 1 == p && n%2==0 && m%2==1){
        cout << "- -" << '\n';
        cout << "C " << m-1 << '\n';
    }
    if (p > c){
        cout << "- -" << '\n';
        cout << "- -" << '\n';
        return 0;
    }
    if (n / 2 < p && n%2==0 && m%2==0){
        cout << "C " << (c-p)*2+1 << '\n';
        cout << "C " << (c-p)*2  << '\n';
        return 0;
    }
    if (n / 2 + 1 < p){
        cout << "C " << (c-p)*2+1 << '\n';
        cout << "C " << (c-p)*2  << '\n';
    }
    return 0;
}
