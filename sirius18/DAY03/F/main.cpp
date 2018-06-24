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
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;



int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m, x;
    set<int> s1, s2, s3;
    cin >> n;
    FI{
        cin >> x;
        s1.insert(x);
    }
    cin >> m;
    FJ{
        cin >> x;
        s2.insert(x);
    }
    for (auto i : s1){
        if (!s2.count(i))
            s3.insert(i);
    }
    for (auto i : s2){
        if (!s1.count(i))
            s3.insert(i);
    }
    cout << s3.size() << '\n';
    if (s3.size())
    for (auto i : s3)
        cout << i << ' ';
}
