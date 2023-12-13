#include <map>
#include <vector>

using namespace std;

class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int count = 0;
        map<int, int> rows;
        map<int, int> cols;
        vector<vector<int>> ones;

        for (int r = 0; r < mat.size(); r ++) {

            for (int c = 0; c < mat[r].size(); c++) {
                if (mat[r][c]) {
                    if (rows.count(r) == 1) {
                        rows[r] += 1;
                    } else {
                        rows[r]= 1;
                    }
                    if (cols.count(c) == 1) {
                        cols[c] += 1;
                    } else {
                        cols[c] = 1;
                    }

                    ones.push_back({r, c});
                }
            }
        }

        for (vector<int> pair : ones) {
            int r = pair[0];
            int c = pair[1];

            if (rows[r] == 1 && cols[c] == 1) {
                count ++;
            }
        }

        return count;
    }
};


int main() {

    


    return 0;
}