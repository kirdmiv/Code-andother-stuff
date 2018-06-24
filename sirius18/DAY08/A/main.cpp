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

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, x1, x2, y1, y2, x, y;
    cin >> n >> x1 >> y1 >> x2 >> y2;
    x1--;y1--;x2--;y2--;
    vector< vector<int> > d(n, vector<int> (n, INF));
    vector< vector<int> > used(n, vector<int> (n, 0));


    vector< vector< pair<int, int> > > prev(n, vector< pair<int, int> > (n, mp(-1, -1)));

    queue< pair<int, int> > q;
    q.push(mp(x1, y1));
    pair<int, int> p;

    int d1[] = {-2, -2, 2, 2, 1, -1, 1, -1};
    int d2[] = {1, -1, 1, -1, -2, -2, 2, 2};

    //for(int i=0; i<8;i++)
    //    cerr << d1[i] << ' ';

    d[x1][y1] = 0;
    used[x1][y1] = 1;
    while (!q.empty()){
        p = q.front();
        q.pop();
        x = p.ff;
        y = p.ss;
        //cerr << x << ' ' << y << '\n';
        for(int i=0; i<8; i++){
            if (-1 < x + d1[i] && x + d1[i] < n
             && -1 < y + d2[i] && y + d2[i] < n && !used[x + d1[i]][y + d2[i]]){
                q.push(mp(x + d1[i], y + d2[i]));
                prev[x + d1[i]][y + d2[i]] = mp(x, y);
                d[x + d1[i]][y + d2[i]] = d[x][y] + 1;
                used[x + d1[i]][y + d2[i]] = 1;
            }
        }
    }
    cout << d[x2][y2] << '\n';
    vector< pair<int, int> > ans;
    x =x2;y=y2;
    ans.pb(mp(x, y));
    while (x != x1 || y != y1){
        //cout << x << ' ' << y << '\n';
        p = prev[x][y];
        x = p.ff;
        y = p.ss;
        ans.pb(mp(x, y));
    }
    reverse(ans.begin(), ans.end());
    for (auto i : ans)
        cout << i.ff+1 << ' ' << i.ss+1 << '\n';
    return 0;
}
