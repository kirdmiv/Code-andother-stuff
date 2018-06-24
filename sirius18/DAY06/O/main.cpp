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
const int n = 9;

vector<int> maxn(9, 0);
vector<int> curn(9, 0);
vector< vector<bool> > used(3, vector<bool> (3, false));

void gen(int p, int i, int j){
    if(maxn < curn)
        maxn = curn;
    if(-1 < i + 1 && i + 1 < 3){
        used[i][j] = false;
        gen(p+1, i+1, j);
        used[i][j] = true;
    }

    if(-1 < i - 1 && i - 1 < 3){
        used[i][j] = false;
        gen(p+1, i-1, j);
        used[i][j] = true;
    }

    if(-1 < j + 1 && j + 1 < 3){
        used[i][j] = false;
        gen(p+1, i, j+1);
        used[i][j] = true;
    }

    if(-1 < j - 1 && j - 1 < 3){
        used[i][j] = false;
        gen(p+1, i, j-1);
        used[i][j] = true;
    }

}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int x;
    vector<int> a[3];
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            cin >> x;
            a[i].pb(x);
        }
    }
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            used[i][j] = false;
            gen(0, i, j);
            used[i][j] = true;
        }
    }
    return 0;
}
