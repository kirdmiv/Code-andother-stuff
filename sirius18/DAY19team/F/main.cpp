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
const int MAXN = 100;


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


    int n, x;
    cin >> n;
    vector<int> used(n+1, 0);
    stack<int> s;

    FI{
        cin >> x;
        if (x > 0){
            used[x] = 0;
            s.push(x);
        }
        if (x == 0 && !s.empty()){
            //cout << s.top();
            s.pop();
        }
        if (x < 0){
            x*=-1;
            used[x] = 1;
        }
        while (!s.empty() && used[s.top()])
                s.pop();
        if (s.empty())
            cout << 0 << '\n';
        else
            cout << s.top() << '\n';
    }

    return 0;
}
