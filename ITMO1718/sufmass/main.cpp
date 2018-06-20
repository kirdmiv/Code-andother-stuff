#include <iostream>
#include <vector>
#include <cstring>

#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define ll long long



using namespace std;

const int maxlen = 1e5;
const int ALPL = 127;

int main()
{
    string s1;
    getline(cin, s1);

    size_t len = s1.size();

    char* s = new char[len+2];

    for(int i=0; i<len; i++){
        s[i] = s1[i];
    }
    s[len] = (char)30;
    s[len+1] = '\0';

    int n = strlen(s);

    int p[maxlen], cnt[maxlen], c[maxlen];
    memset(cnt, 0, ALPL * sizeof(int));
    for (int i=0; i<n; ++i)
        ++cnt[s[i]];
    for (int i=1; i<ALPL; ++i)
        cnt[i] += cnt[i-1];
    for (int i=0; i<n; ++i)
        p[--cnt[s[i]]] = i;
    c[p[0]] = 0;
    int classes = 1;
    for (int i=1; i<n; ++i) {
        if (s[p[i]] != s[p[i-1]])  ++classes;
        c[p[i]] = classes-1;
    }

    int pn[maxlen], cn[maxlen];
    for (int h=0; (1<<h)<n; ++h) {
        for (int i=0; i<n; ++i) {
            pn[i] = p[i] - (1<<h);
            if (pn[i] < 0)  pn[i] += n;
        }
        memset (cnt, 0, classes * sizeof(int));
        for (int i=0; i<n; ++i)
            ++cnt[c[pn[i]]];
        for (int i=1; i<classes; ++i)
            cnt[i] += cnt[i-1];
        for (int i=n-1; i>=0; --i)
            p[--cnt[c[pn[i]]]] = pn[i];
        cn[p[0]] = 0;
        classes = 1;
        for (int i=1; i<n; ++i) {
            int mid1 = (p[i] + (1<<h)) % n,  mid2 = (p[i-1] + (1<<h)) % n;
            if (c[p[i]] != c[p[i-1]] || c[mid1] != c[mid2])
                ++classes;
            cn[p[i]] = classes-1;
        }
        memcpy(c, cn, n * sizeof(int));
    }
    for(int i=1; i<n; i++){
        cout << p[i]+1 << " ";
    }
}
