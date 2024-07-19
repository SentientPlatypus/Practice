#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        vector<int> colm(matrix[0].size(), -1);
        vector<int> rowm(matrix.size(), -1);


        vector<int>ret;


        for (int r = 0; r < matrix.size(); r++) {
            if (rowm[r] == -1) rowm[r] = *min_element(matrix[r].begin(), matrix[r].end());
            
            for (int c = 0; c < matrix[r].size(); c++) {
                if (colm[c] == -1) {
                    int m = -1;
                    for (int i = 0; i < matrix.size(); i++) {
                        m = max(m, matrix[i][c]);
                    }
                    colm[c] = m;
                }

                if (matrix[r][c] == colm[c] && matrix[r][c]== rowm[r]) ret.push_back(matrix[r][c]);
            }
        }        
        return ret;
    }
};