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

    int n, x = 0;
    char s;
    deque<int> p1, p2;
    cin >> n;
    FI{
        cin >> s;
        if (s == '+' || s == '*')
            cin >> x;
        else{
            //cout << p1.size() << '\n';
            cout << p1.front() << '\n';
            p1.pop_front();
            }
        if(s == '+'){
            p2.push_back(x);
        }
        if(s == '*'){
            if (p1.size() > p2.size())
                p2.push_front(x);
            else
                p2.push_back(x);
        }
        if (p2.size() + ((p2.size() + p1.size())%2)> p1.size()){
            p1.push_back(p2.front());

            p2.pop_front();}
        else if (p1.size() > p2.size()){
            p2.push_front(p1.back());
            p1.pop_back();
        }
        //for (int i : p1) cout << i << ' ';
        //cout << '\n';
        //for (int i : p2) cout << i << ' ';
        //cout << '\n';

    }

    return 0;
}
