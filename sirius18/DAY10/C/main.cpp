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
    int type, x;
    Event (int t, int y) : type(t), x(y) {}

    bool operator< (const Event& oth) const{
        return (x < oth.x) || ((x == oth.x) && type > oth.type);
    }
};

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, h1, m1, s1, h2, m2, s2, cnt=0;
    vector<Event> e;
    cin >> n;
    FI{
        cin >> h1 >> m1 >> s1 >> h2 >> m2 >> s2;
        m1 += h1 * 60;
        s1 += m1 * 60;
        m2 += h2 * 60;
        s2 += m2 * 60;

        if (s1 == s2){
            cnt++;
            continue;
        }
        if (s1 > s2){
            e.eb(Event(1, 0));
            e.eb(Event(-1, 86400));
        }
        e.eb(Event(1, s1));
        e.eb(Event(-1, s2));
    }

    stable_sort(e.begin(), e.end());
    int l=0, ans=0, bal=0;
    if (cnt == n)
        ans = 86400;
    //cout << cnt << '\n';
    for(auto i : e){
        if (i.type == 1)
            l = i.x;
        if (i.type == 1){
            bal++;
            cnt++;
        }
        else{
            bal--;
            cnt--;
        }
        if (cnt == n-1 && i.type == -1)//{//{
            ans += i.x - l;
            //cout <<i.x <<' '<<cnt<< '\n';//cout << ans << ' ' << l << ' ' << bal << ' '<< i.x<<'\n';}
        //cout << i.x << '\n';
        //}
    }

    cout << ans;
    return 0;
}
