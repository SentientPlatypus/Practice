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

    int a, b;
    std::cin >> a >> b;

    int n;
    std::cin >> n;

    int v[n+2];
    v[0] = 0;
    for(int i = 1; i <= n; i++)
        std::cin >> v[i];
    v[n+1] = a;
    
    int m;
    std::cin >> m;
    
    int h[m+2];
    h[0] = 0;
    for(int i = 1; i <= m; i++)
        std::cin >> h[i];
    h[m+1] = b;
    
    int ans = -RAND_MAX;
    for(int i = 1; i <= m+1; i++) {
        int dh = h[i] - h[i-1];
        for(int j = 1; j <= n+1; j++) {
            int dv = v[j] - v[j-1];
            ans = std::max(dh * dv, ans);
        }
    }

    std::cout << ans << "\n";

	return 0;
}