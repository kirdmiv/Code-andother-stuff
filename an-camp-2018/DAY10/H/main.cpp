#include <iostream>
#include <vector>

using namespace std;

vector<int> a, ans_a;
int n, k;
vector<bool> used;

void gen(int k1, int last){
    if (k1 == k){
        for (int i=0; i<k; i++){
            cout << a[i] << " ";
    }
    cout << endl;
    return;
    }
    for (int i=last+1; i<n+1; i++){
        if (!used[i] && n+1-i >= k-k1){
            a.push_back(i);
            used[i] = true;
            gen(k1 + 1, i);
            used[i] = false;
            a.pop_back();
        }
    }

}

int main()
{
    freopen("choose.in", "r", stdin);
    freopen("choose.out", "w", stdout);

    cin >> n >> k;
    used.resize(n);
    for (int i=0; i<n; i++){
        used.push_back(false);
    }
    gen(0, 0);


    return 0;
}
