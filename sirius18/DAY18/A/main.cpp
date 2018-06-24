#include <bits/stdc++.h>
#include "ext/rope"
#include "ext/pb_ds/detail/standard_policies.hpp"
#include "ext/pb_ds/assoc_container.hpp"

#define np nullptr
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

//file define
//#define INPUT_FILE "stdin.in"
//#define OUTPUT_FILE "stdout.out"

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


void print(const vector<int> &v, char sep=' ', char end=' '){
    for (auto i : v){
        cout << i << sep;
    }
    cout << '\n';
}



const int INF = 1e9;
const int MAXN = 100001;


/*
░░░░░░░░░
░░░░▄▀▀▀▀▀█▀▄▄▄▄░░░░
░░▄▀▒▓▒▓▓▒▓▒▒▓▒▓▀▄░░
▄▀▒▒▓▒▓▒▒▓▒▓▒▓▓▒▒▓█░
█▓▒▓▒▓▒▓▓▓░░░░░░▓▓█░
█▓▓▓▓▓▒▓▒░░░░░░░░▓█░
▓▓▓▓▓▒░░░░░░░░░░░░█░
▓▓▓▓░░░░▄▄▄▄░░░▄█▄▀░
░▀▄▓░░▒▀▓▓▒▒░░█▓▒▒░░
▀▄░░░░░░░░░░░░▀▄▒▒█░
░▀░▀░░░░░▒▒▀▄▄▒▀▒▒█░
░░▀░░░░░░▒▄▄▒▄▄▄▒▒█░
░░░▀▄▄▒▒░░░░▀▀▒▒▄▀░░
░░░░░▀█▄▒▒░░░░▒▄▀░░░
░░░░░░░░▀▀█▄▄▄▄▀ KappaPRIDE(no tsveta ne vidno)

*/


/*
░░▄▄▄▄▄▓▓▓▄▄▄░░░░░
░░░░▄▄▓▀▀▀▀▀▀▓▓▓▓▓▓▄░░░
░░▄▄▓▀▀░░░░░░░▒▒▒▒▒▀▓▄░
░▐▓▓▌░░░░░░░░░░░░▒▒▒▒▓▌
░▐▓▒░░▄▒▒▓▄▄▒▒▒░▒▄▄▄▒▒▓
░▓▓▌░░░░░▒▒▒▒▀▒▒▓▓▓▓▓▓▓
░▐▓░░░░▒▒▓(◐)▓░░░▒▓▓(◐)▒▓
█░▀▄░█▄█▀▄▄░▀░▀▄▄▀░░█░█
░█░░░▀▄█▄█░█▀▄▄▄▄▄▀██░█
░░█░░░░█░███▄█▄█▄███░░█
░░░█░░░▀▀█░█▀█▀█▀███░█
░░░░▀▄░░░░▀▀▄█▄█▄█▄▀░█
░░░░░░▀▄▄░▒▒▒░░░░░░░░░█
░░░░░░░░░▀▀▄▄▄▄▄▄▄▄▄▄▀
*/


/*
Спасибо, мистер Дудец!
░░░░░░▄▄▄░░▄██▄░░░
░░░░░▐▀█▀▌░░░░▀█▄░░░
░░░░░▐█▄█▌░░░░░░▀█▄░░
░░░░░░▀▄▀░░░▄▄▄▄▄▀▀░░
░░░░▄▄▄██▀▀▀▀░░░░░░░
░░░█▀▄▄▄█░▀▀░░
░░░▌░▄▄▄▐▌▀▀▀░░
▄░▐░░░▄▄░█░▀▀ ░░
▀█▌░░░▄░▀█▀░▀ ░░
░░░░░░░▄▄▐▌▄▄░░░
░░░░░░░▀███▀█░▄░░
░░░░░░▐▌▀▄▀▄▀▐▄░░
░░░░░░▐▀░░░░░░▐▌░░
░░░░░░█░░░░░░░░█░░░
*/


int n, x, q, l, r;
vector<int> a;
vector< pair<int, int> > b(MAXN, mp(0, 0));
int k = 300;
int m = ceil(n/k);

/*
░░░░░░░░░
░░░░▄▀▀▀▀▀█▀▄▄▄▄░░░░
░░▄▀▒▓▒▓▓▒▓▒▒▓▒▓▀▄░░
▄▀▒▒▓▒▓▒▒▓▒▓▒▓▓▒▒▓█░
█▓▒▓▒▓▒▓▓▓░░░░░░▓▓█░
█▓▓▓▓▓▒▓▒░░░░░░░░▓█░
▓▓▓▓▓▒░░░░░░░░░░░░█░
▓▓▓▓░░░░▄▄▄▄░░░▄█▄▀░
░▀▄▓░░▒▀▓▓▒▒░░█▓▒▒░░
▀▄░░░░░░░░░░░░▀▄▒▒█░
░▀░▀░░░░░▒▒▀▄▄▒▀▒▒█░
░░▀░░░░░░▒▄▄▒▄▄▄▒▒█░
░░░▀▄▄▒▒░░░░▀▀▒▒▄▀░░
░░░░░▀█▄▒▒░░░░▒▄▀░░░
░░░░░░░░▀▀█▄▄▄▄▀ KappaPRIDE(no tsveta ne vidno)

*/



void build(){
    for(int i=0; i<n; i++){
        int j = i/k;
        if (a[i] == b[j].ff)
            b[j].ss++;
        else if (a[i] > b[j].ff){
            b[j] = mp(a[i], 1);
        }
    }
}

/*
Спасибо, мистер Дудец!
░░░░░░▄▄▄░░▄██▄░░░
░░░░░▐▀█▀▌░░░░▀█▄░░░
░░░░░▐█▄█▌░░░░░░▀█▄░░
░░░░░░▀▄▀░░░▄▄▄▄▄▀▀░░
░░░░▄▄▄██▀▀▀▀░░░░░░░
░░░█▀▄▄▄█░▀▀░░
░░░▌░▄▄▄▐▌▀▀▀░░
▄░▐░░░▄▄░█░▀▀ ░░
▀█▌░░░▄░▀█▀░▀ ░░
░░░░░░░▄▄▐▌▄▄░░░
░░░░░░░▀███▀█░▄░░
░░░░░░▐▌▀▄▀▄▀▐▄░░
░░░░░░▐▀░░░░░░▐▌░░
░░░░░░█░░░░░░░░█░░░
*/




int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    #ifdef INPUT_FILE
    freopen(INPUT_FILE, "r", stdin);
    #endif // INPUT_FILE

    #ifdef OUTPUT_FILE
    freopen(OUTPUT_FILE, "w", stdout);
    #endif // OUTPUT_FILE


    cin >> n;
    FI{
        cin >> x;
        a.eb(x);
    }
    build();
    cin >> q;
    int cnt=0, maxe=0, b_l, b_r;
    for(int i = 0; i<q; i++){
        cin >> l >> r;
        l--; r--;
        cnt = 0;
        maxe = 0;
        b_l = l/k; b_r = r/k;
        if (b_l == b_r){
            for(int j=l; j<=r; ++j){
                if(maxe == a[j])
                    cnt++;
                else if (maxe < a[j]){
                    maxe = a[j];
                    cnt = 1;
                }
            }
        } else {
            int lend = ((b_l+1) * k)-1;
            for(int j=l; j<=lend; ++j){
                if(maxe == a[j])
                    cnt++;
                else if (maxe < a[j]){
                    maxe = a[j];
                    cnt = 1;
                }
            }

            for(int j=b_l+1; j<=b_r-1; ++j){
                if(maxe == b[j].ff)
                    cnt += b[j].ss;
                else if (maxe < b[j].ff){
                    maxe = b[j].ff;
                    cnt = b[j].ss;
                }
            }

            int rbeg = ((b_r) * k);
            for(int j=rbeg; j<=r; ++j){
                if(maxe == a[j])
                    cnt++;
                else if (maxe < a[j]){
                    maxe = a[j];
                    cnt = 1;
                }
            }
        }
        cout << maxe << ' ' << cnt << '\n';
    }



    return 0;
}
