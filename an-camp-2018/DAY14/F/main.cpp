#include <bits/stdc++.h>

int main() {
    freopen("maxnumber.in", "r", stdin);
    freopen("maxnumber.out", "w", stdout);
    int n;
    scanf("%d", &n);
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    long long result = 0;
    std::map<int, long long> sum;
    std::vector<int> div2;
    for (int i = 0; i < n; i++) {
        int x = a[i];
        while (x % 2 == 0) {
            x /= 2;
        }
        if (sum.find(x) == sum.end()) {
            div2.push_back(x);
        }
        sum[x] += a[i] / x;
    }
    for (int x : div2) {
        int power = 0;
        long long number = 1;
        while (number * 2 <= sum[x]) {
            power++;
            number <<= 1LL;
        }
        result = std::max(result, x * 1LL * number);
    }
    std::cout << result << '\n';
}
