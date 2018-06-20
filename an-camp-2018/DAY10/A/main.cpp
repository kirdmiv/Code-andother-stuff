#include <iostream>
#include <vector>

using namespace std;

vector<int> a, ans_a;
int n, r, max_res;
vector<bool> used;

void gen(int res){
    if (a.size() == n){
        res %= r;
        if (res > max_res){
            max_res = res;
            ans_a = a;
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
    freopen("optimal.in", "r", stdin);
    freopen("optimal.out", "w", stdout);

    cin >> n >> r;
    max_res = 0;
    used.resize(n);
    for (int i=0; i<n; i++){
        used.push_back(false);
    }
    gen(0);

    if (ans_a.size() != n){
        for (int i=1; i<n+1; i++){
        ans_a.push_back(i);
        int s = 0;
        if (i > 0){
                s = (i-1) * i;
            }
        max_res += s;
        }
        max_res %= r;

        cout << max_res << endl;

        for (int i=0; i<n; i++){
            cout << ans_a[i] << " ";
        }
        return 0;
    }
    cout << max_res << endl;

    for (int i=0; i<n; i++){
        cout << ans_a[i] << " ";
    }
    return 0;
}
