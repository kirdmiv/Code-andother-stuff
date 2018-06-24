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

    int n, m, x, y, stx, sty, a;
    cin >> n >> m;
    vector<int> g[n];
    FI{
        FJ{
            cin >> a;
            g[i].pb(a);
        }
    }
    vector< vector<int> > d(n, vector<int> (n, INF));
    vector< vector<int> > used(n, vector<int> (n, 0));


    vector< vector< pair<int, int> > > prev(n, vector< pair<int, int> > (n, mp(-1, -1)));

    queue< pair<int, int> > q;
    q.push(mp(0, 0));
    pair<int, int> p;

    int d1[] = {1, -1, 0, 0};
    int d2[] = {0, 0, -1, 1};

    //for(int i=0; i<8;i++)
    //    cerr << d1[i] << ' ';

    d[0][0] = 0;
    used[0][0] = 1;
    while (!q.empty()){
        p = q.front();
        q.pop();
        stx = x = p.ff;
        sty = y = p.ss;
        //cerr << x << ' ' << y << '\n';
        for(int i=0; i<4; i++){
            x = stx;
            y = sty;
            while(-1 < x + d1[i] && x + d1[i] < n
             && -1 < y + d2[i] && y + d2[i] < n && !used[x + d1[i]][y + d2[i]] && !(g[x + d1[i]][y + d2[i]] != 1))
                x++;y++;
             if (0 > x + d1[i] || x + d1[i] >= n
             ||  0 > y + d2[i] || y + d2[i] >= n || g[x + d1[i]][y + d2[i]] == 1){
                q.push(mp(x + d1[i], y + d2[i]));
                prev[x + d1[i]][y + d2[i]] = mp(x, y);
                d[x][y + d2[i]] = d[x][y] + 1;
                used[x + d1[i]][y + d2[i]] = 1;
            }
        }
    }
    int mans;
    FI{
        FJ{
            if (g[i][j] == 2)
                mans = min(mans, d[i][j]);
        }
    }
    cout << mans;
    return 0;
}
