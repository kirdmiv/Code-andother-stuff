#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

vector<int> a;
int n, r, max_res;
vector<bool> used;

void gen(int res){
    if (a.size() == n){
        res %= r;



            int delitleli = 0;
            int sq = sqrt(res);
            float sq_f = sqrt(res);
            for (int i=1; i <= sq; i++){
            if ((res % i) == 0){
                if ((float)i == sq_f){
                    delitleli++;
                }
                else{
                    delitleli++;delitleli++;
                }
            }


            }
            if (delitleli % 3 == 0){
                max_res += 1;
            }

        return;
    }
    for (int i=1; i<n+1; i++){
        if (!used[i]){
            a.push_back(i);
            used[i] = true;
            int s = 0;
            int size_a = a.size();
            if (size_a > 1){
                s = a[size_a - 2] * a[size_a - 1];
            }
            gen(res + s);
            used[i] = false;
            a.pop_back();
        }
    }

}

int main()
{
    freopen("beautiful.in", "r", stdin);
    freopen("beautiful.out", "w", stdout);

    cin >> n >> r;
    max_res = 0;
    used.resize(n);
    for (int i=0; i<n; i++){
        used.push_back(false);
    }
    gen(0);

    cout << max_res;

    return 0;
}
