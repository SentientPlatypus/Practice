#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> r;
        r.push_back({1});

        for (int i = 1; i < numRows; i++) {
            vector<int> newlist;
            newlist.push_back(1);


            for (int k = 1; k < r[i - 1].size(); k++) {
                newlist.push_back(r[i - 1][k] + r[i - 1][k - 1]);
            }

            newlist.push_back(1);
            r.push_back(newlist);
        }
        return r;
    }
};


int main() {
    cout << "hello" << endl;
}