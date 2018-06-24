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

struct Event{
    int x, y;
    Event (int a, int b) : x(a), y(b) {}

    bool operator< (const Event& oth) const{
        return (x < oth.x) || ((x == oth.x) && y < oth.y);
    }
};

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int m, a, b, n;
    vector<Event> e, ans;
    cin >> m;
    while (true){
        cin >> a >> b;
        if(a == 0 && b == 0)
            break;
        e.eb(Event(a, b));
    }
    n = e.size();
    stable_sort(e.begin(), e.end());
    int cur, bal=0, l=0, maxr, maxl;
    for(int i =0; i<n; i++){
        cur = e[i].x;
        maxr = e[i].y;
        maxl = e[i].x;
        while (i < n-1 && cur <= l){
            if (maxr < e[i].y){
                maxr = e[i].y;
                maxl = e[i].x;
            }
            i += 1;
            cur = e[i].x;
        }
        l = maxr;
        ans.eb(Event(maxl, maxr));

    }
    if (l < m){
        cout << "No solution\n";
        return 0;
    }
    cout << ans.size() << '\n';
    for (auto i : ans)
        cout << i.x << ' ' << i.y << '\n';
    return 0;
}
