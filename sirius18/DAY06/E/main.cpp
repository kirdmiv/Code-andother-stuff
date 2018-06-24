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

const int MAXN = 15;

char a[MAXN];
stack<char> s;
int n;

void gen(int p, int b1, int b2){
    if(p>n) return;
    if (p == n && b1 == 0 && b2 == 0){
        FI{
            cout << a[i];
        }
        cout << '\n';
        return;
    }
    //cout << p <<"\n";
    if(n - p >= b1 + b2){
        a[p] = '(';
        s.push('(');
        gen(p+1, b1+1, b2);
        s.pop();
    }

    if(n - p >= b1 + b2){
        a[p] = '[';
        s.push('[');
        gen(p+1, b1, b2+1);
        s.pop();
    }

    if(b1 > 0 && s.top() == '('){
        s.pop();
        a[p] = ')';
        gen(p+1, b1-1, b2);
        s.push('(');
    }

    if(b2 > 0 && s.top() == '['){
        s.pop();
        a[p] = ']';
        gen(p+1, b1, b2-1);
        s.push('[');
    }
    //cout << p <<"\n";
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    gen(0, 0, 0);

    return 0;
}
