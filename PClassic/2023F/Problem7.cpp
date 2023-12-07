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

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);
	std::cout.tie(NULL);

	int N; std::cin >> N;

    int v[N], c[N];
    int maxh = -RAND_MAX;
    for(int i = 0; i < N; i++) {
        std::cin >> v[i];
        maxh = std::max(v[i], maxh);
        if(i > 0)
            c[i] = (v[i] < maxh); // 1 for covered
    }
    
    int argmax, max = -RAND_MAX;
    for(int n = 0; n < N; n++) {
        if(c[n]) continue;
        int h = -RAND_MAX, k = 0;
        for(int i = 0; i < N; i++) {
            if(i == n) continue;
            if(h < v[i]) {
                h = v[i];
                k++;
            }
        }
        if(max < k) {
            max = k;
            argmax = n;
        }
    }

    std::cout << argmax + 1 << "\n";

	return 0;
}