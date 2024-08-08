#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        vector<vector<int>> res;
        vector<vector<int>> dir{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int direction = 0;
        for (int step = 1; res.size() < rows * cols; ++step) {
            for (int i = 0; i < 2; ++i) {
                for (int j = 0; j < step; ++j) {
                    if (rStart >= 0 && rStart < rows && cStart >= 0 && cStart < cols) {
                        res.push_back({rStart, cStart});
                    }
                    rStart += dir[direction][0];
                    cStart += dir[direction][1];
                }
                direction = (direction + 1) % 4;
            }
        }
        return res;
    }
};
