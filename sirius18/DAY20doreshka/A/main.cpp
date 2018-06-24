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
const int MAXN = 10;


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

int n;
int res =0;
vector< vector<int> > used(MAXN,  vector<int> (MAXN, 0) );
vector< pair<int, int> > a;

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


void genus(int num, int ln){
    //cout << ln << ' ' << num << '\n';
    if (num == n){
        res++;
        int m = n;
        //FI {FJ cout << used[i][j]<<' ';cout<<'\n';}
        //cout << '\n';
        return;
    }
    FI{
        if(!used[ln][i]){
            int m = n;
            FJ{
                used[j][i] = 1;
            }
            int sr = ln, st = i;
            while (0<=sr && sr <n && 0<=st && st<n){
                used[sr][st] = 1;
                sr++;
                st++;
            }
            sr = ln, st = i;
            while (0<=sr && sr <n && 0<=st && st<n){
                used[sr][st] = 1;
                sr++;
                st--;
            }
            sr = ln, st = i;
            while (0<=sr && sr <n && 0<=st && st<n){
                used[sr][st] = 1;
                sr--;
                st++;
            }
            sr = ln, st = i;
            while (0<=sr && sr <n && 0<=st && st<n){
                used[sr][st] = 1;
                sr--;
                st--;
            }

            genus(num+1, ln+1);

            FJ{
                used[j][i] = 0;
            }
            sr = ln, st = i;
            while (0<=sr && sr <n && 0<=st && st<n){
                used[sr][st] = 0;
                sr++;
                st++;
            }
            sr = ln, st = i;
            while (0<=sr && sr <n && 0<=st && st<n){
                used[sr][st] = 0;
                sr++;
                st--;
            }
            sr = ln, st = i;
            while (0<=sr && sr <n && 0<=st && st<n){
                used[sr][st] = 0;
                sr--;
                st++;
            }
            sr = ln, st = i;
            while (0<=sr && sr <n && 0<=st && st<n){
                used[sr][st] = 0;
                sr--;
                st--;
            }

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


int check(int i, int j){
    for (auto k : a){
        if (k.ff == i || k.ss == j)
            return 0;
        int sr = k.ff, st = k.ss;
        while (0<=sr && sr <n && 0<=st && st<n){
            if (sr == i && st == j)
                return 0;
            sr++;
            st--;
        }
        sr = k.ff, st = k.ss;
        while (0<=sr && sr <n && 0<=st && st<n){
            if (sr == i && st == j)
                return 0;
            sr++;
            st++;
        }
        sr = k.ff, st = k.ss;
        while (0<=sr && sr <n && 0<=st && st<n){
            if (sr == i && st == j)
                return 0;
            sr--;
            st--;
        }
        sr = k.ff, st = k.ss;
        while (0<=sr && sr <n && 0<=st && st<n){
            if (sr == i && st == j)
                return 0;
            sr--;
            st++;
        }
    }
    return 1;
}


void gen(int num, int ln){
    if (num == n){
        res++;
        //int m = n;
        //FI {FJ cout << used[i][j]<<' ';cout<<'\n';}
        //cout << '\n';
        return;
    }
    FI{
        if (check(ln, i)){
            a.pb(mp(ln, i));
            gen(num+1, ln+1);
            a.pop_back();
        }
    }
}


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
    gen(0, 0);

    cout << res;

    return 0;
}
