#include <string>
using namespace std;

class Solution {
public:
    int possibleStringCount(string word) {
        int ans = 0;
        for (int i = 1; i < word.size(); i++) {
            if (word[i - 1] == word[i]) {
                ans++;
            }
        }
        return ans + 1;

    }
};