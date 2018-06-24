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

vector<char> a;
int n;
void nextp(){
    //cout << 'ok';
    int i = n - 2;
    while (i > -1 && a[i] >= a[i+1])
        i-=1;
    //cout << n;
    if (i < 0){
        reverse(a.begin(), a.end());
        FI{
            cout << a[i];
        }
        cout << '\n';
        return;
    }
    int j = n - 1;
    while (a[j] <= a[i])
        j-=1;
    int tmp = a[i];
    a[i] = a[j];
    a[j] = tmp;
    //cout << i << ' ' << j;
    reverse(a.begin() + i+1, a.end());
    FI{
        cout << a[i];
    }
    cout << '\n';
}


int main()
{
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);

    string s;
    while(cin >> s){
        n = s.size();
        a.resize(n);
        for(int i= 0; i<n;i++){
            a[i] = s[i];
            //cout << a[i];
        }
        nextp();
    }
    return 0;
}
