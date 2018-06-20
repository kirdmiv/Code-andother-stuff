#include <iostream>
#include<vector>

using namespace std;

const int MAXN = 1002;
const int INF = 1000000000;
int dp [MAXN][MAXN] ;
int main(){
    int n, m;
    scanf("%d%d", &m, &n);
    vector <int> a(m);
    for (int i = 0 ; i < m; i++) {
        scanf("%d", &a[i]);
    }
    for (int i = 0 ; i <= n; i++) {
        fill(dp[i], dp [i] + m + 1 , -INF) ;
    }
    dp[0][0] = 0;
    for (int i = 0 ; i < n; i++) {
        for ( int j = 0; j < m; j++) {
            if (dp[i][j] == -INF) {
                continue;
            }
            dp[i+1][0] = max(dp[i + 1][0], dp[i][j]);
            int rew = a[j % m];
            dp [i + 1] [( j + 1 ) % m] = max( dp[ i + 1 ][ ( j + 1 ) % m], dp[i][j] + rew);
        }
    }
    int mx = 0 ;
    for (int i = 0 ; i < m; i++) {
    mx = max(mx, dp[n][i]) ;
    }
    cout << mx << endl;
    return 0 ;
}

