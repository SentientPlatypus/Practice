#include <vector>
#include <queue>
#include <iostream>

using namespace std;

class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        int n = stones.size();
        int comp = 0;

        vector<bool> visited(n, false);

        for (int i = 0; i < n; i++) {
            queue<int> q;
            q.push(i);
            visited[i] = true;

            while (!q.empty()) {
                int cur = q.front();
                q.pop();

                for (int k = 0; k < n; k++) {
                    if (k != i && !visited[k] && (stones[i][0] == stones[k][0] || stones[i][1] == stones[k][1]) ) {
                        
                    }
                }


            }
        }
    }
};