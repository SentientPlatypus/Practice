#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        vector<vector<int>> m(rowSum.size(), vector<int>(colSum.size(), 0));

        int i = 0, j = 0;

        while (i < rowSum.size() && j < colSum.size()) {
            m[i][j] = min(rowSum[i], colSum[j]);

            rowSum[i] -= m[i][j];
            colSum[j] -= m[i][j];

            rowSum[i] == 0 ? i++ : j++;
        }
        return m;


    }
};