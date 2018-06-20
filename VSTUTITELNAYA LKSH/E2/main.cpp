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

char mode;
ll n,m,i,l,r,x,t[4 * MAX], delta[4 * MAX];
vector<int> a;
int xx;

void pull(int v){
    //cerr << v;
    t[v] = t[2*v+1] + t[2*v];
}


void build(int v, int l, int r){
    if (l == r - 1){
        //cerr << l;
        t[v] = a[l];
        return;
    }
    int m = (l + r) / 2;
    //cerr << v << ' ';
    build(2*v, l, m);
    //cerr << v << ' ';
    build(2*v+1, m, r);
    //cerr << v << ' ';
    pull(v);
}





void push(ll v, ll k){
	if(delta[v] != -1){
		t[v*2] = delta[v]*(k-(k/2));
		t[v*2+1] = delta[v]*(k/2);
		delta[v*2] = delta[v];
		delta[v*2+1] = delta[v];
		delta[v] = -1;
	}
}

void update(ll v, ll l, ll r, ll lt, ll rt, ll x){
	if((lt <= l) && (rt >= r) && (delta[v] != -1)){
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
        delta[v]=-1;
	t[v] = t[v*2] + t[v*2+1];
}

ll sum(ll v, ll l, ll r, ll lt, ll rt){
	if((lt<=l)&&(rt>=r)) return t[v];
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
	cin >> n;
	//for(int i=0; i<n;i++) { cin >> xx; a.emplace_back(x);}
	//build(1, 0, n);
	cin >> m;
	for(i = 0; i < m; i++){
		cin >> mode >> l >> r;
		if(mode == '1'){
			cin >> x;
			update(1, 0, n, l, r, x);
		} else{
			cout << sum(1, 0, n, l, r) << '\n';
		}
	}
}
