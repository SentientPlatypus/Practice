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

	int m; std::cin >> m;

    int p; 
    std::cin >> p;
    int px[p];
    for(int i = 0; i < p; i++)
        std::cin >> px[i];
    
    int q; 
    std::cin >> q;
    int qx[q];
    for(int i = 0; i < q; i++)
        std::cin >> qx[i];
    
    for(int &x: qx)
        m += x;
    for(int &x: px)
        m *= x;

    std::cout << m << "\n";

	return 0;
}