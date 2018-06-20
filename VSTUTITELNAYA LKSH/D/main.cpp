#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <utility>
#include <functional>
#include <set>
#include <string>
#include <math.h>
#include <cmath>

#define mp make_pair
#define ff first
#define ss second
#define ll long long
#define pb push_back

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    vector <int> a(n, 0);
    for (size_t i = 0; i < n; i++){
        cin >> a[i];
    }
    if (!(n<=k<=2*n)){
        cout << "Impossible";
        return 0;
    }
    vector< vector<int> > d(k, vector<int> tmp(0, k));
    for(int i = 0; i < k; i++){
        for(int j = 0; j < k; j++){

        }
    }
    return 0;
}
