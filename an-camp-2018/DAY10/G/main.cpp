#include <iostream>
#include <vector>

using namespace std;

int main()
{
    freopen("crypto.in", "r", stdin);
    freopen("crypto.out", "w", stdout);

    int n, a, b;
    cin >> n >> a >> b;

    int maxim = -1;
    int s;
    int maxx = 1;
    int maxy = 1;
    for (int x=1; x<n+1; x++){
        for (int y=x; y>0; y=(y-1)&x){
            //cout << x << " " << y<<endl;

            if ((((a&x + b&y) ^ (a&y + b&x)) > maxim)){
                maxim = ((a&x + b&y) ^ (a&y + b&x));
                maxx = x;
                maxy = y;

            }
        }
    }

    cout << maxx << " " << maxy;
    return 0;
}
