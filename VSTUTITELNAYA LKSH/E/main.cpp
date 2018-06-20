#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <fstream>
#include <utility>
#include <functional>
#include <set>
#include <string>
#include <bits/stdc++.h>

#define mp make_pair
#define ff first
#define ss second
#define ll long long
#define pb push_back
#define MAX 100010

using namespace std;
long long t[4*MAX];

long long sum(int Vertex, int LeftPos, int RightPos, int Left, int Right)
{
  if (Left > Right) return 0;
  if ((Left == LeftPos) && (Right == RightPos))
    return t[Vertex];
  int Middle = (LeftPos + RightPos) / 2;
  return sum(2*Vertex, LeftPos, Middle, Left, min(Right,Middle)) +
         sum(2*Vertex+1, Middle+1, RightPos, max(Left,Middle+1), Right);

}

void update(int Vertex, int LeftPos, int RightPos, int Position, int NewValue)
{
  if (LeftPos == RightPos)
    t[Vertex] = NewValue;
  else
  {
    int Middle = (LeftPos + RightPos) / 2;
    if (Position <= Middle) update (2*Vertex, LeftPos, Middle, Position, NewValue);
    else update (2*Vertex+1, Middle+1, RightPos, Position, NewValue);
    t[Vertex] = t[2*Vertex] + t[2*Vertex+1];
  }
}


int n, k;
long long i, j, l, r, x;
char c;
int main (void) {
    memset(t,0,sizeof(t));
    cin >> n >> k;

    for(j = 0; j < k; j++) {
        cin >> c;
        if (c == '1') {
            cin >> i >> x;
            update(1,1,n,i,x);
        }
        else {
            cin >> l >> r;
            printf("%lld\n",sum(1,1,n,l,r));
        }
    }
  return 0;
}
