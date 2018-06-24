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
        return (x < oth.x) || ((x == oth.x) && y > oth.y);
    }
};

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int m, a, b, n;
    vector<Event> e;
    stack<Event> st;
    cin >> n;
    vector<int> ans(n, -1);
    ull res=0, c;
    FI{
        cin >> a >> b;
        e.eb(Event(a, b, i));
    }
    n = e.size();
    stable_sort(e.begin(), e.end());
    int cur, bal=0, l=0, curr=e[0].y, curl=e[0].x, curn=e[0].num;
    //st.push(e[0]);
    for(int i =0; i<n; i++){
        while (!st.empty() && st.top().y < e[i].y)
            st.pop();
        if (!st.empty())
            ans[e[i].num] = st.top().num;
        st.push(e[i]);
    }
    for (auto i : ans)
        cout << i+1 << ' ';
    return 0;
}
