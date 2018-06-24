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

vector< vector<bool> > a(100, vector<bool> (100, false));

int n;
int gen(int p){
    int res = 0;
    if(p == n){
        return 1;
    }
    for(int i = 0; i<n; i++){
        for(int j = 0; j<n; j++){
            if(!a[i][j]){
                int k = i, l = j;
                while (k < n && l < n){
                    a[k][l] = false;
                    k++;
                    l++;
                }
                while (k > -1 && l < n){
                    a[k][l] = false;
                    k--;
                    l++;
                }
                while (k > -1 && l > -1){
                    a[k][l] = false;
                    k--;
                    l--;
                }
                while (k < n && l > -1){
                    a[k][l] = false;
                    k++;
                    l--;
                }
                for(int k = 0; i<n; i++){
                    a[i][k] = false;
                }
                for(int k = 0; j<n; j++){
                    a[k][j] = false;
                }

                res += gen(p+1);

                l = i-j;
                k = i, l = j;
                while (k < n && l < n){
                    a[k][l] = true;
                    k++;
                    l++;
                }
                while (k > -1 && l < n){
                    a[k][l] = true;
                    k--;
                    l++;
                }
                while (k > -1 && l > -1){
                    a[k][l] = true;
                    k--;
                    l--;
                }
                while (k < n && l > -1){
                    a[k][l] = true;
                    k++;
                    l--;
                }
                for(int k = 0; i<n; i++){
                    a[i][k] = true;
                }
                for(int k = 0; j<n; j++){
                    a[k][j] = true;
                }

            }
        }
    }
    return res;
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;

    cout << gen(0);
    return 0;
}
