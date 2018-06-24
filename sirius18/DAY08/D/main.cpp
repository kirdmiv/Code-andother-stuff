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

    string s1, s2;
    int n, x1, x2, y1, y2, x, y;
    n=8;
    cin >> s1 >> s2;
    x1 = s1[0] - 'a';
    x2 = s2[0] - 'a';

    y1 = s1[1] - '1';
    y2 = s2[1] - '1';
    //cout << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << '\n';
    vector< vector<int> > d(n, vector<int> (n, INF));
    vector< vector<int> > d3(n, vector<int> (n, INF));
    vector< vector<int> > used(n, vector<int> (n, 0));
    vector< vector<int> > used3(n, vector<int> (n, 0));


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
                d[x + d1[i]][y + d2[i]] = d[x][y] + 1;
                used[x + d1[i]][y + d2[i]] = 1;
            }
        }
    }

    queue< pair<int, int> > q1;
    q1.push(mp(x2, y2));
    d3[x2][y2] = 0;
    used3[x2][y2] = 1;
    while (!q1.empty()){
        p = q1.front();
        q1.pop();
        x = p.ff;
        y = p.ss;
        //cerr << x << ' ' << y << '\n';
        for(int i=0; i<8; i++){
            if (-1 < x + d1[i] && x + d1[i] < n
             && -1 < y + d2[i] && y + d2[i] < n && !used3[x + d1[i]][y + d2[i]]){
                q1.push(mp(x + d1[i], y + d2[i]));
                d3[x + d1[i]][y + d2[i]] = d3[x][y] + 1;
                used3[x + d1[i]][y + d2[i]] = 1;
            }
        }
    }

    int mind = INF;
    int m = n;
    FI{
        FJ{
            if (d[i][j] == d3[i][j])
                mind = min(mind, d3[i][j]);
        }
    }
    if (mind == INF)
        cout << -1;
    else
        cout << mind;
    //cout << d[x2][y2] << '\n';
    return 0;
}
