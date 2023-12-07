#include <bits/stdc++.h>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>

int n, k;
int maxr = -RAND_MAX;
int ans = -RAND_MAX;

std::vector<int> v;

void solve(int i, int dx, int t, int sum) {
    if(i+dx >= n) return;

    sum += v[i+dx];
    if(t == k) {
        ans = std::max(sum, ans);
        return;
    }

    ans = std::max(sum + (k-t)*v[i+dx], ans);
    if(v[i+dx] == maxr)
        return;
    
    solve(i+dx, 1, t+1, sum);
}

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);
	std::cout.tie(NULL);

    std::cin >> n >> k;

    v.resize(n);
    for(int i = 0; i < n; i++) {
        std::cin >> v[i];
        maxr = std::max(v[i], maxr);
    }

    solve(0, 0, 1, 0);
    solve(0, 1, 1, 0);

    std::cout << ans << "\n";

	return 0;
}