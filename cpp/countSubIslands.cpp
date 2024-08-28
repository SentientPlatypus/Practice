#include <vector>
#include <queue>
using namespace std;


class Solution {
public:
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int count = 0;
        for (int r = 0; r < grid2.size(); r++) {
            for (int c = 0; c < grid2[0].size(); c++) {
                if (grid2[r][c]) {
                    bool subIsland = true;
                    //found an island
                    queue<pair<int,int>> q;

                    q.push({r,c});
                    grid2[r][c] = 0;
                    
                    while (!q.empty()) { //traverses entire island
                        pair<int, int> cur = q.front();
                        q.pop();


                        if (!grid1[cur.first][cur.second]) {
                            subIsland = false; //check if grid1 has all cells in the island
                        }

                        //add all other island cells to queue
                        for (pair<int, int> p : neighbors(cur.first, cur.second, grid2)) {
                            grid2[p.first][p.second] = 0;
                            q.push(p);
                        }
                    }
                    if (subIsland) count++;
                }

            }
        }
        return count;
    }

    vector<pair<int, int>> neighbors(int r, int c, vector<vector<int>>& grid) {
        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        vector<pair<int, int>> res;

        for (pair<int, int> p : directions) {
            int row = r + p.first;
            int column = c + p.second;
            if (row >= 0 && row < grid.size() && column >= 0 && column < grid[0].size() && grid[row][column] == 1) {
                res.push_back({row, column});
            }
        }
        return res;
    }
};