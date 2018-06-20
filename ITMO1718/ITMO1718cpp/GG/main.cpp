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
#include <queue>

#define mp make_pair
#define ff first
#define ss second
#define ll long long
#define pb push_back
#define st size_t
#define FI for(int i = 0; i < n; i++)

using namespace std;
int n;

int main(){
    int x, y;
    cin >> n;
    FI cin >> x >> y;
    if (n == 3 || n == 4)
    cout << 1;
    else
    cout << 2;
    return 0;
}
