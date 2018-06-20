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

vector<int> z_function (string s) {
	int n = (int) s.length();
	vector<int> z (n);
	for (int i=1, l=0, r=0; i<n; ++i) {
		if (i <= r)
			z[i] = min (r-i+1, z[i-l]);
		while (i+z[i] < n && s[z[i]] == s[i+z[i]])
			++z[i];
		if (i+z[i]-1 > r)
			l = i,  r = i+z[i]-1;
	}
	return z;
}

int main()
{
    string s;
    getline(cin, s);
    vector<int> z = z_function(s);
    vector< pair<int, int> > lz;
    z[0] = s.length();
    size_t pointer = 0;
    for(size_t i = 0; i < z.size(); i++){
        if (z[i] != 0){
            int m = z[i] / 2 - 1;
            if( z[i] % 2 != 0){
                m++;
            }
            //cout << i << " " << i+m;
            lz.pb(mp(i, i+m));
        }
        while(pointer < lz.size() && lz[pointer].ss < i) pointer++;
        if (pointer < lz.size()){
            cout << 2*(i - lz[pointer].ff) + 1<< " ";
        }
        if (pointer >= lz.size()){
            cout << 0 << " ";
        }
    }
    return 0;
}
