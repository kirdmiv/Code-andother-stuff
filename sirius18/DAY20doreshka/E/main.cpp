#include<iostream>
#include<string>
#include<algorithm>
#include<stdio.h>
#include<stdlib.h>
#include<iomanip>
#include<math.h>
#include <cstdio>
#include <cstring>
#include <vector>
#include <fstream>
#include <utility>
#include <functional>
#include <set>

#define mp make_pair
#define ff first
#define ss second
#define ll long long
#define pb push_back
#define MAX 100010

using namespace std;

const ll INF = 2e18;

char mode;
ll n,m,i,l,r,x,t[4 * MAX], delta[4 * MAX];

void push(ll v, ll k){
    if(delta[v] != -INF){
        t[v*2] += delta[v]*(k-(k/2));
        t[v*2+1] += delta[v]*(k/2);
        delta[v*2] = delta[v];
        delta[v*2+1] = delta[v];
        delta[v] = -INF;
    }
}

void update(ll v, ll l, ll r, ll lt, ll rt, ll x){
    if((lt <= l) && (rt >= r) && (delta[v] != -INF)){
        delta[v]=x;
        t[v]=(r-l+1)*x;
        return;
    }
    push(v, r-l+1);
    ll mid=(l+r)/2;

    if(lt<=mid) update(v*2, l, mid, lt, rt, x);

    if(rt>mid) update(v*2+1, mid+1, r, lt, rt, x);

    if(delta[v*2] == delta[v*2+1])
        delta[v] = delta[v*2];
    else
        delta[v]=-INF;
    t[v] = t[v*2] + t[v*2+1];
}

ll sum(ll v, ll l, ll r, ll lt, ll rt){
    if((lt<=l)&&(rt>=r)) return (t[v]);

    push(v,r-l+1);
    ll mid = (l+r)/2;
    ll s = 0;
    if(lt <= mid)
        s += sum(v*2, l, mid, lt, rt);
    if(rt > mid)
        s += sum(v*2+1, mid+1, r, lt, rt);
    return s;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    for(i = 0; i < m; i++){
        cin >> mode >> l >> r;
        if(mode == '1'){
            cin >> x;
            update(1, 0, n, l, r, x);
        } else{
            cout << sum(1, 0, n, l, r) << '\n';
        }
        for (int i=0; i<4*n; i++){
            cout << t[i] << ' ';
        } cout << '\n';
    }
}
