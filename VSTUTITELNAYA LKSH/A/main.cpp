#include <stdlib.h>
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
#define pb push_back
#define eb emplace_back
#define st size_t

using namespace std;
typedef long long ll;
const double PI = 3.14159265358979323846;

struct point {
    ll x, y;
    point() {
        x = y = 0;
    }
    point(ll _x, ll _y) {
        x = _x;
        y = _y;
    }
    ll operator*(point p) {
        return (ll) x * p.y - (ll) y * p.x;
    }
    point operator-(point p) {
        return point(x - p.x, y - p.y);
    }
    point operator+(point p) {
        return point(x + p.x, y + p.y);
    }
};

int main()
{
    st n;
    cin >> n;
    ll x, y;
    ll sq = 0;
    vector<point> inp;
    for (st j = 0; j < n; j++) {
        cin >> x >> y;
        inp.eb(point(x, y));
    }
    for (st j = 0; j < n; j++) {
        st next = (j + 1) % n;
        sq += ((inp[j].x - inp[next].x) * (inp[j].y + inp[next].y));
    }
    sq = labs(sq);
    st ans1 = 0, ans2 = 1;
    st pointer = 1;
    ll cur_sq1 = 0, cur_sq2 = sq, new_sq1, new_sq2, tr_sq, tr_sqi;
    ll max_sq1 = cur_sq1, max_sq2 = cur_sq2;
    for (st i = 0; i < n; i++){
        while (pointer < n){
            st next = (pointer + 1) % n;
            tr_sq = labs((inp[pointer]-inp[i]) * (inp[next]-inp[i]));
            new_sq1 = cur_sq1 + tr_sq;
            new_sq2 = cur_sq2 - tr_sq;
            //cout << tr_sq << " " << i << " " << pointer << " " << new_sq1 << " " << new_sq2 << " " << cur_sq1 << " " << cur_sq2<< " "<<labs(cur_sq1 - cur_sq2) << endl;
            //double res1 = (double)new_sq1/new_sq2, res2 = (double)cur_sq1/cur_sq2;
            if (labs(new_sq1 - new_sq2) < labs(max_sq1 - max_sq2)){
                    ans1 = i;
                    ans2 = pointer+1;
                    max_sq1 = new_sq1;
                    max_sq2 = new_sq2;
            }
            if (labs(new_sq1 - new_sq2) < labs(cur_sq1 - cur_sq2) && new_sq1 <= new_sq2){
                //cout << tr_sq << " " << i << " " << next << " " << new_sq1 << " " << new_sq2 << " " << cur_sq1 << " " << cur_sq2<< " "<<labs(cur_sq1 - cur_sq2) << endl;
                cur_sq1 = new_sq1;
                cur_sq2 = new_sq2;
                //cout << tr_sq << " " << i << " " << next << " " << new_sq1 << " " << new_sq2 << " " << cur_sq1 << " " << cur_sq2<< " "<<labs(cur_sq1 - cur_sq2) << endl;
                if (pointer < n)
                    pointer++;
            }
            else
                break;
        }
        st nexti = (i + 1) % n;
        tr_sqi = labs((inp[nexti]-inp[i]) * (inp[pointer%n]-inp[i]));
        cur_sq1 -= tr_sqi;
        cur_sq2 += tr_sqi;
        //cout << cur_sq1 << " " << cur_sq2 << endl;
    }
    cout << (ans1%n) + 1 << " " << (ans2%n)+1;
    return 0;
}
