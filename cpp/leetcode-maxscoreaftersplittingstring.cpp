#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxScore(string s) {
        int maxs = 0;
        int count_zeros = 0;
        int count_ones = count(s.begin(), s.end(), '1');
        for (int i = 0; i < s.length() - 1; i ++) {
            count_zeros += (s[i] == '0');
            count_ones -= (s[i] == '1');
            maxs = max(maxs, count_zeros + count_ones);
        }
        return maxs;
    }
};

