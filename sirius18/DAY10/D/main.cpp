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

const int INF = 2e9;

struct Event{
    int x, y, num;
    Event (int a, int b, int n) : x(a), y(b), num(n) {}

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
    cin >> n;
    ull res=0, c;
    FI{
        cin >> a >> b >> c;
        e.eb(Event(a, a+b, i));
    }
    n = e.size();
    stable_sort(e.begin(), e.end());
    int cur, bal=0, l=0, curr=e[0].y, curl=e[0].x, curn=e[0].num;
    for(int i =1; i<n; i++){
        if (e[i].x >= curr){
            ans.eb(Event(curr, curl, curn));
            res += c;
            l = curr;
            curr=e[i].y; curl=e[i].x; curn=e[i].num;
        }
        if (l <= e[i].x && e[i].y < curr){
            curr=e[i].y; curl=e[i].x; curn=e[i].num;
        }
    }
    ans.eb(Event(curr, curl, curn));
    res += c;
    cout << res << '\n';
    cout << ans.size() << '\n';
    for (auto i : ans)
        cout << i.num+1 << ' ';
    return 0;
}
